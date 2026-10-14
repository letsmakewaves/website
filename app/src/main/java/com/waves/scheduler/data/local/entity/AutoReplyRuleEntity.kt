package com.waves.scheduler.data.local.entity

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey
import com.waves.scheduler.domain.model.TargetScope
import com.waves.scheduler.domain.model.TriggerType

/**
 * An inbound auto-reply rule. Replies are delivered through each channel's
 * official inbound webhook / messaging API (WhatsApp Cloud, Telegram Bot),
 * within those platforms' session-messaging windows — not by injecting text
 * into another app's notifications.
 *
 * [cooldownMinutes] is anti-loop protection: the same sender is not answered
 * more than once per window, preventing two bots from ping-ponging forever.
 */
@Entity(
    tableName = "auto_reply_rules",
    indices = [Index("isEnabled")],
)
data class AutoReplyRuleEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val title: String,
    @ColumnInfo(defaultValue = "1") val isEnabled: Boolean = true,
    /** JSON array of ChannelType names this rule listens on. */
    val channelTypesJson: String,
    val triggerType: TriggerType,
    /** JSON array of keywords/phrases (ignored when triggerType is ALL). */
    @ColumnInfo(defaultValue = "NULL") val keywordsJson: String? = null,
    val replyText: String,
    @ColumnInfo(defaultValue = "0") val useAiReply: Boolean = false,
    @ColumnInfo(defaultValue = "NULL") val aiSystemPrompt: String? = null,
    val targetScope: TargetScope = TargetScope.BOTH,
    /** JSON array of contact keys to exclude. */
    @ColumnInfo(defaultValue = "NULL") val excludedContactsJson: String? = null,
    @ColumnInfo(defaultValue = "60") val cooldownMinutes: Int = 60,
    /** JSON active-hours/days window; null = always active. */
    @ColumnInfo(defaultValue = "NULL") val activeScheduleJson: String? = null,
)
