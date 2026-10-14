package com.waves.scheduler.data.local.dao

import androidx.room.Dao
import androidx.room.Embedded
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Relation
import androidx.room.Transaction
import androidx.room.Update
import com.waves.scheduler.data.local.entity.AttachmentEntity
import com.waves.scheduler.data.local.entity.RecipientEntity
import com.waves.scheduler.data.local.entity.ScheduledTaskEntity
import com.waves.scheduler.domain.model.DeliveryStatus
import com.waves.scheduler.domain.model.TaskStatus
import kotlinx.coroutines.flow.Flow

/** A task with everything the execution engine needs, loaded in one read. */
data class TaskWithDetails(
    @Embedded val task: ScheduledTaskEntity,
    @Relation(parentColumn = "id", entityColumn = "taskId")
    val recipients: List<RecipientEntity>,
    @Relation(parentColumn = "id", entityColumn = "taskId")
    val attachments: List<AttachmentEntity>,
)

@Dao
interface ScheduledTaskDao {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTask(task: ScheduledTaskEntity): Long

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertRecipients(recipients: List<RecipientEntity>)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAttachments(attachments: List<AttachmentEntity>)

    /** Persist a task and its children atomically; returns the new task id. */
    @Transaction
    suspend fun insertFullTask(
        task: ScheduledTaskEntity,
        recipients: List<RecipientEntity>,
        attachments: List<AttachmentEntity>,
    ): Long {
        val taskId = insertTask(task)
        insertRecipients(recipients.map { it.copy(taskId = taskId) })
        insertAttachments(attachments.map { it.copy(taskId = taskId) })
        return taskId
    }

    @Update
    suspend fun updateTask(task: ScheduledTaskEntity)

    @Query("UPDATE scheduled_tasks SET status = :status, updatedAtMillis = :now WHERE id = :taskId")
    suspend fun updateStatus(taskId: Long, status: TaskStatus, now: Long = System.currentTimeMillis())

    @Query(
        """
        UPDATE recipients
        SET deliveryStatus = :status, deliveredAtMillis = :deliveredAt, errorReason = :error
        WHERE id = :recipientId
        """,
    )
    suspend fun updateRecipientDelivery(
        recipientId: Long,
        status: DeliveryStatus,
        deliveredAt: Long?,
        error: String?,
    )

    @Transaction
    @Query("SELECT * FROM scheduled_tasks WHERE id = :taskId")
    suspend fun getTaskWithDetails(taskId: Long): TaskWithDetails?

    @Transaction
    @Query("SELECT * FROM scheduled_tasks ORDER BY scheduledEpochMillis ASC")
    fun observeTasks(): Flow<List<TaskWithDetails>>

    @Query("SELECT * FROM scheduled_tasks WHERE status = :status ORDER BY scheduledEpochMillis ASC")
    suspend fun getTasksByStatus(status: TaskStatus): List<ScheduledTaskEntity>

    /** Used after reboot to re-arm every alarm that has not yet fired. */
    @Query("SELECT * FROM scheduled_tasks WHERE status = 'PENDING'")
    suspend fun getPendingTasks(): List<ScheduledTaskEntity>

    @Query("DELETE FROM scheduled_tasks WHERE id = :taskId")
    suspend fun deleteTask(taskId: Long)
}
