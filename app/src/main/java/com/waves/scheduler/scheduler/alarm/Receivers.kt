package com.waves.scheduler.scheduler.alarm

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import dagger.hilt.android.AndroidEntryPoint

/**
 * Skeletons for the scheduling coordinator (full logic in Part 3).
 *
 * - [TaskAlarmReceiver] fires at a task's exact time and enqueues the send.
 * - [BootCompletedReceiver] re-arms PENDING alarms after reboot/app update.
 * - [AskBeforeSendReceiver] handles the Send/Snooze actions on the
 *   "Ask before sending" notification.
 */

@AndroidEntryPoint
class TaskAlarmReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // Part 3: resolve taskId -> enqueue ExecutionService / WorkManager job.
    }
}

@AndroidEntryPoint
class BootCompletedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // Part 3: re-arm all PENDING task alarms.
    }
}

@AndroidEntryPoint
class AskBeforeSendReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // Part 3: on SEND_NOW enqueue the task; on SNOOZE re-schedule it.
    }
}
