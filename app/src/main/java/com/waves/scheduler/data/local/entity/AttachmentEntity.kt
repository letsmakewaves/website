package com.waves.scheduler.data.local.entity

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey

/**
 * A file attached to a task. [uriString] is a content:// URI held under a
 * persisted read grant (ContentResolver.takePersistableUriPermission) so it
 * survives until the task fires.
 */
@Entity(
    tableName = "attachments",
    foreignKeys = [
        ForeignKey(
            entity = ScheduledTaskEntity::class,
            parentColumns = ["id"],
            childColumns = ["taskId"],
            onDelete = ForeignKey.CASCADE,
        ),
    ],
    indices = [Index("taskId")],
)
data class AttachmentEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val taskId: Long,
    val uriString: String,
    val mimeType: String,
    @ColumnInfo(defaultValue = "NULL") val displayName: String? = null,
    @ColumnInfo(defaultValue = "0") val fileSize: Long = 0,
)
