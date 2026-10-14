package com.waves.scheduler.data.local

import android.content.Context
import androidx.room.Room
import com.waves.scheduler.data.local.dao.AutoReplyDao
import com.waves.scheduler.data.local.dao.ScheduledTaskDao
import com.waves.scheduler.data.local.dao.TemplateDao
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): WavesDatabase =
        Room.databaseBuilder(context, WavesDatabase::class.java, WavesDatabase.NAME)
            // A real migration path replaces this before the first store release.
            .fallbackToDestructiveMigration()
            .build()

    @Provides fun provideScheduledTaskDao(db: WavesDatabase): ScheduledTaskDao = db.scheduledTaskDao()
    @Provides fun provideAutoReplyDao(db: WavesDatabase): AutoReplyDao = db.autoReplyDao()
    @Provides fun provideTemplateDao(db: WavesDatabase): TemplateDao = db.templateDao()
}
