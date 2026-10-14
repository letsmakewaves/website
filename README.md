# Waves Scheduler

An Android message-scheduling and auto-reply app in the spirit of SKEDit —
schedule messages across channels, set keyword auto-replies, reuse templates,
and compose with an AI assistant.

## Architecture note (important)

SKEDit drives WhatsApp/Telegram/Instagram by automating their on-screen UI
through Android's **Accessibility API**. That approach has two hard problems:
it only works while the phone is unlocked (no PIN/pattern/password), and it
violates those platforms' terms of service, which gets accounts banned.

**Waves Scheduler uses each platform's official API instead:**

| Channel | Transport |
| --- | --- |
| WhatsApp / WA Business | WhatsApp Business Cloud API (Meta Graph) |
| Telegram | Telegram Bot API |
| Instagram / Messenger | Meta Graph API (business/creator accounts) |
| SMS | Android `SmsManager` |
| Email | SMTP / Gmail API |

The result keeps working on a locked phone, in the background, without risking
bans — at the cost of requiring platform business accounts and consented
(opt-in) recipients for the chat channels.

## Tech stack

Kotlin · Jetpack Compose · Room · WorkManager + AlarmManager · Hilt ·
Coroutines/Flow · Retrofit/OkHttp · kotlinx.serialization.

## Build status by part

- [x] **Part 1** — Project structure, Gradle/version catalog, `AndroidManifest.xml`
- [x] **Part 2** — Room entities, DAOs, TypeConverters, database + DI
- [ ] **Part 3** — AlarmManager/WorkManager scheduling coordinator & channel senders
- [ ] **Part 4** — Inbound auto-reply dispatcher (official webhooks)
- [ ] **Part 5** — Jetpack Compose UI (composer, calendar, rules, setup wizard)

## Module layout

```
app/src/main/java/com/waves/scheduler/
├── WavesSchedulerApp.kt            # Hilt + WorkManager app entry point
├── domain/model/                   # Channel/status/trigger enums
├── data/local/
│   ├── entity/                     # 6 Room entities
│   ├── dao/                        # ScheduledTask, AutoReply, Template DAOs
│   ├── converter/                  # enum TypeConverters
│   ├── WavesDatabase.kt
│   └── DatabaseModule.kt           # Hilt DB/DAO providers
├── scheduler/                      # (Part 3) alarm receivers + execution service
└── ui/                             # (Part 5) Compose screens; MainActivity host
```
