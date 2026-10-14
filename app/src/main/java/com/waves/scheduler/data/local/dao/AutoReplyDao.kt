package com.waves.scheduler.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import com.waves.scheduler.data.local.entity.AutoReplyLogEntity
import com.waves.scheduler.data.local.entity.AutoReplyRuleEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface AutoReplyDao {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsertRule(rule: AutoReplyRuleEntity): Long

    @Update
    suspend fun updateRule(rule: AutoReplyRuleEntity)

    @Query("UPDATE auto_reply_rules SET isEnabled = :enabled WHERE id = :ruleId")
    suspend fun setEnabled(ruleId: Long, enabled: Boolean)

    @Query("DELETE FROM auto_reply_rules WHERE id = :ruleId")
    suspend fun deleteRule(ruleId: Long)

    @Query("SELECT * FROM auto_reply_rules ORDER BY id DESC")
    fun observeRules(): Flow<List<AutoReplyRuleEntity>>

    /** Active rules only — the inbound dispatcher evaluates these against each message. */
    @Query("SELECT * FROM auto_reply_rules WHERE isEnabled = 1")
    suspend fun getEnabledRules(): List<AutoReplyRuleEntity>

    @Insert
    suspend fun insertLog(log: AutoReplyLogEntity)

    /**
     * Most recent reply timestamp for a sender under a rule. Returns null if the
     * rule never answered this sender; used to enforce the cooldown window.
     */
    @Query(
        """
        SELECT MAX(timestampMillis) FROM auto_reply_logs
        WHERE ruleId = :ruleId AND senderKey = :senderKey
        """,
    )
    suspend fun lastReplyAt(ruleId: Long, senderKey: String): Long?

    @Query("SELECT * FROM auto_reply_logs ORDER BY timestampMillis DESC LIMIT :limit")
    fun observeRecentLogs(limit: Int = 200): Flow<List<AutoReplyLogEntity>>
}
