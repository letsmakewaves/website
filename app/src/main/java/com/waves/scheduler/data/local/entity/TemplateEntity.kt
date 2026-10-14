package com.waves.scheduler.data.local.entity

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey

/**
 * A reusable message template. [bodyText] may contain {{placeholders}} that are
 * resolved against a recipient's custom variables at send time.
 */
@Entity(
    tableName = "templates",
    indices = [Index("category")],
)
data class TemplateEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val title: String,
    val bodyText: String,
    @ColumnInfo(defaultValue = "'General'") val category: String = "General",
    val createdAtMillis: Long = System.currentTimeMillis(),
)
