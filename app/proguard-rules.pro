# Keep kotlinx.serialization generated serializers.
-keepattributes *Annotation*, InnerClasses
-dontnote kotlinx.serialization.**
-keepclassmembers class **$$serializer { *; }
-keepclasseswithmembers class com.waves.scheduler.** {
    kotlinx.serialization.KSerializer serializer(...);
}

# JavaMail / activation referenced reflectively.
-dontwarn javax.activation.**
-dontwarn com.sun.mail.**
-keep class com.sun.mail.** { *; }
-keep class javax.mail.** { *; }
-keep class javax.activation.** { *; }

# Retrofit / OkHttp.
-dontwarn okhttp3.**
-dontwarn okio.**
-keepattributes Signature, Exceptions
