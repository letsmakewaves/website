package com.waves.scheduler.ui

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import dagger.hilt.android.AndroidEntryPoint

/**
 * Single-activity host. The real navigation graph and screens (composer,
 * calendar, auto-reply rules, setup wizard) land in Part 5; this placeholder
 * keeps Parts 1–2 runnable.
 */
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Scaffold { inner ->
                    Column(
                        modifier = Modifier.fillMaxSize().padding(inner).padding(24.dp),
                        verticalArrangement = Arrangement.Center,
                        horizontalAlignment = Alignment.CenterHorizontally,
                    ) {
                        Placeholder()
                    }
                }
            }
        }
    }
}

@Composable
private fun Placeholder() {
    Text("Waves Scheduler", style = MaterialTheme.typography.headlineMedium)
    Text("Data layer ready — UI arrives in Part 5.", style = MaterialTheme.typography.bodyMedium)
}
