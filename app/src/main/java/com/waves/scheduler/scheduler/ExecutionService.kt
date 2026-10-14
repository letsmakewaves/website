package com.waves.scheduler.scheduler

import android.app.Service
import android.content.Intent
import android.os.IBinder
import dagger.hilt.android.AndroidEntryPoint

/**
 * Foreground service that runs one scheduled task's recipients to completion
 * through the appropriate official-API channel sender. Full implementation
 * (notification, channel dispatch, per-recipient status writes) lands in Part 3.
 */
@AndroidEntryPoint
class ExecutionService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // Part 3: promote to foreground, dispatch the task, then stopSelf().
        return START_NOT_STICKY
    }
}
