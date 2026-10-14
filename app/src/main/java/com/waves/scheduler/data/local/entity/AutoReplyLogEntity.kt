package com.waves.scheduler.data.local.entity

import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey

/**
 * Audit trail of fired auto-replies. Also the source of truth for cooldown:
 * before replying, the engine checks the latest log row for [senderKey] on the
 * rule and suppresses if still inside the cooldown window.
 */
@Entity(
    tableName = "auto_reply_logs",
    foreignKeys = [
        ForeignKey(
            entity = AutoReplyRuleEntity::class,
            parentColumns = ["id"],
            childColumns = ["ruleId"],
            onDelete = ForeignKey.CASCADE,
        ),
    ],
    indices = [Index("ruleId"), Index(value = ["ruleId", "senderKey", "timestampMillis"])],
)
data class AutoReplyLogEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val ruleId: Long,
    /** Stable per-conversation key (channel + sender address). */
    val senderKey: String,
    val incomingText: String,
    val repliedText: String,
    val timestampMillis: Long = System.currentTimeMillis(),
)
