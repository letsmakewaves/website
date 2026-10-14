package com.waves.scheduler.data.local.entity

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey
import com.waves.scheduler.domain.model.ChannelType
import com.waves.scheduler.domain.model.ExecutionMode
import com.waves.scheduler.domain.model.TaskStatus

/**
 * A single scheduled send (one-off or one step of a recurring/drip series).
 *
 * [repeatRuleJson] holds a serialized recurrence rule (interval, by-day,
 * stop condition). [dripCampaignId] and [stepIndex] link steps of a
 * multi-message sequence; both are null for standalone tasks.
 */
@Entity(
    tableName = "scheduled_tasks",
    indices = [
        Index("status"),
        Index("scheduledEpochMillis"),
        Index("dripCampaignId"),
    ],
)
data class ScheduledTaskEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val title: String,
    val channelType: ChannelType,
    val executionMode: ExecutionMode,
    val bodyText: String,
    val scheduledEpochMillis: Long,
    @ColumnInfo(defaultValue = "NULL") val repeatRuleJson: String? = null,
    val status: TaskStatus = TaskStatus.PENDING,
    @ColumnInfo(defaultValue = "NULL") val dripCampaignId: Long? = null,
    @ColumnInfo(defaultValue = "0") val stepIndex: Int = 0,
    /** Occurrences already fired, for "stop after N" recurrence. */
    @ColumnInfo(defaultValue = "0") val occurrenceCount: Int = 0,
    val createdAtMillis: Long = System.currentTimeMillis(),
    val updatedAtMillis: Long = System.currentTimeMillis(),
)
