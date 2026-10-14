package com.waves.scheduler.data.local.converter

import androidx.room.TypeConverter
import com.waves.scheduler.domain.model.ChannelType
import com.waves.scheduler.domain.model.DeliveryStatus
import com.waves.scheduler.domain.model.ExecutionMode
import com.waves.scheduler.domain.model.TargetScope
import com.waves.scheduler.domain.model.TaskStatus
import com.waves.scheduler.domain.model.TriggerType

/**
 * Enum <-> String converters. Enums are stored by [Enum.name] (not ordinal) so
 * reordering or inserting enum constants never corrupts existing rows.
 */
class Converters {
    @TypeConverter fun channelToString(v: ChannelType): String = v.name
    @TypeConverter fun stringToChannel(v: String): ChannelType = ChannelType.valueOf(v)

    @TypeConverter fun execModeToString(v: ExecutionMode): String = v.name
    @TypeConverter fun stringToExecMode(v: String): ExecutionMode = ExecutionMode.valueOf(v)

    @TypeConverter fun taskStatusToString(v: TaskStatus): String = v.name
    @TypeConverter fun stringToTaskStatus(v: String): TaskStatus = TaskStatus.valueOf(v)

    @TypeConverter fun deliveryToString(v: DeliveryStatus): String = v.name
    @TypeConverter fun stringToDelivery(v: String): DeliveryStatus = DeliveryStatus.valueOf(v)

    @TypeConverter fun triggerToString(v: TriggerType): String = v.name
    @TypeConverter fun stringToTrigger(v: String): TriggerType = TriggerType.valueOf(v)

    @TypeConverter fun scopeToString(v: TargetScope): String = v.name
    @TypeConverter fun stringToScope(v: String): TargetScope = TargetScope.valueOf(v)
}
