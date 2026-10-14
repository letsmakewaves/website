package com.waves.scheduler.domain.model

/**
 * Delivery channels. Each maps to an official, policy-compliant transport in the
 * data layer — no third-party app UIs are driven and no accounts are automated
 * in a way that violates a platform's terms.
 */
enum class ChannelType {
    /** WhatsApp Business Cloud API (Meta Graph). Templated/session messaging with opt-in. */
    WHATSAPP_CLOUD,

    /** Telegram Bot API. */
    TELEGRAM_BOT,

    /** Android [android.telephony.SmsManager]. */
    SMS,

    /** SMTP or Gmail API. */
    EMAIL,

    /** Instagram Messaging via Meta Graph API (business/creator accounts). */
    INSTAGRAM_GRAPH,

    /** Facebook Messenger Platform (Meta Graph API). */
    MESSENGER_GRAPH,
}

/** How a task is dispatched when its scheduled time arrives. */
enum class ExecutionMode {
    /** Send automatically in the background via the channel's API. */
    AUTO,

    /** Post a notification with Send / Snooze actions; nothing leaves until confirmed. */
    ASK_FIRST,
}

/** Lifecycle of a scheduled task. */
enum class TaskStatus {
    PENDING,
    RUNNING,
    COMPLETED,
    PARTIAL_FAILURE,
    FAILED,
    PAUSED,
}

/** Per-recipient outcome within a task. */
enum class DeliveryStatus {
    QUEUED,
    SENT,
    DELIVERED,
    FAILED,
    SKIPPED,
}

/** How an inbound auto-reply rule matches incoming text. */
enum class TriggerType {
    EXACT,
    CONTAINS,
    STARTS_WITH,
    REGEX,
    /** Catch-all: matches any inbound message in scope. */
    ALL,
}

/** Which conversations an auto-reply rule applies to. */
enum class TargetScope {
    INDIVIDUAL,
    GROUP,
    BOTH,
}
