package com.waves.scheduler.data.local.entity

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import com.waves.scheduler.domain.model.DeliveryStatus

/**
 * One target of a [ScheduledTaskEntity]. The engine messages recipients
 * sequentially and records a per-row [deliveryStatus] so a retried task can
 * resume only the rows that did not succeed.
 *
 * [customVariablesJson] carries CSV merge fields (e.g. {"Name":"Ada"}) used to
 * render placeholders like {{Name}} in the task body — for sending to one's own
 * opted-in contacts, not unsolicited bulk outreach.
 */
@Entity(
    tableName = "recipients",
    foreignKeys = [
        ForeignKey(
            entity = ScheduledTaskEntity::class,
            parentColumns = ["id"],
            childColumns = ["taskId"],
            onDelete = ForeignKey.CASCADE,
        ),
    ],
    indices = [Index("taskId"), Index("deliveryStatus")],
)
data class RecipientEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val taskId: Long,
    val displayName: String,
    @ColumnInfo(defaultValue = "NULL") val phoneNumber: String? = null,
    /** Platform-specific address: email, Telegram chat id, WA phone id, etc. */
    @ColumnInfo(defaultValue = "NULL") val channelAddress: String? = null,
    @ColumnInfo(defaultValue = "0") val isGroup: Boolean = false,
    @ColumnInfo(defaultValue = "NULL") val customVariablesJson: String? = null,
    val deliveryStatus: DeliveryStatus = DeliveryStatus.QUEUED,
    @ColumnInfo(defaultValue = "NULL") val deliveredAtMillis: Long? = null,
    @ColumnInfo(defaultValue = "NULL") val errorReason: String? = null,
)
