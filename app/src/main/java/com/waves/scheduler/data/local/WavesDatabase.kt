package com.waves.scheduler.data.local

import androidx.room.Database
import androidx.room.RoomDatabase
import androidx.room.TypeConverters
import com.waves.scheduler.data.local.converter.Converters
import com.waves.scheduler.data.local.dao.AutoReplyDao
import com.waves.scheduler.data.local.dao.ScheduledTaskDao
import com.waves.scheduler.data.local.dao.TemplateDao
import com.waves.scheduler.data.local.entity.AttachmentEntity
import com.waves.scheduler.data.local.entity.AutoReplyLogEntity
import com.waves.scheduler.data.local.entity.AutoReplyRuleEntity
import com.waves.scheduler.data.local.entity.RecipientEntity
import com.waves.scheduler.data.local.entity.ScheduledTaskEntity
import com.waves.scheduler.data.local.entity.TemplateEntity

@Database(
    entities = [
        ScheduledTaskEntity::class,
        RecipientEntity::class,
        AttachmentEntity::class,
        AutoReplyRuleEntity::class,
        AutoReplyLogEntity::class,
        TemplateEntity::class,
    ],
    version = 1,
    exportSchema = true,
)
@TypeConverters(Converters::class)
abstract class WavesDatabase : RoomDatabase() {
    abstract fun scheduledTaskDao(): ScheduledTaskDao
    abstract fun autoReplyDao(): AutoReplyDao
    abstract fun templateDao(): TemplateDao

    companion object {
        const val NAME = "waves_scheduler.db"
    }
}
