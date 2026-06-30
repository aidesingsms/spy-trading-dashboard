#!/bin/bash
TELEGRAM_BOT_TOKEN="8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk"
TELEGRAM_CHANNEL="@aidesing_alerts"

cd /root/.openclaw/workspace
openclaw sessions_spawn --agentId main --mode run --runtime subagent --label "fed-check-$(date +%H%M)" --task "Monitorea noticias de FED, política monetaria, datos económicos (CPI, PPI, NFP), declaraciones de miembros FED. Genera alerta si detectas cambio en política o datos sorpresa. Formato: 🏦 ALERTA [NIVEL] | Evento: [desc] | Impacto: [mercados] | Señal: [acción] | Canal: @aidesing_alerts"
