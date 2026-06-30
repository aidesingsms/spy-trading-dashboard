# Configuración Webhook TradingView

## Fecha: 2026-06-26
## Estado: Configurando

---

## Información del Webhook

**URL del Webhook:**
```
https://api.telegram.org/bot8682815952:AAEYO8E_YbFpOb2i1xmbMvvNntIa9208kOk/sendMessage?chat_id=@aidesing_alerts
```

**Método:** POST
**Content-Type:** application/json

---

## Configuración en TradingView

### Paso 1: Crear Alerta
1. Abre tu gráfico en TradingView
2. Click en el icono de alerta (campana)
3. Configura las condiciones de la alerta

### Paso 2: Configurar Notificación
1. En "Mensaje", escribe el formato deseado
2. Activa "Webhook URL"
3. Pega la URL proporcionada arriba
4. Guarda la alerta

---

## Formato de Mensaje Recomendado

```
📈 ALERTA TRADINGVIEW

Activo: {{ticker}}
Precio: {{close}}
Timeframe: {{interval}}

Condición: [tu condición]

⏰ {{time}}
```

---

## Variables Disponibles (TradingView)

- `{{ticker}}` - Símbolo del activo
- `{{close}}` - Precio de cierre
- `{{open}}` - Precio de apertura
- `{{high}}` - Máximo
- `{{low}}` - Mínimo
- `{{volume}}` - Volumen
- `{{time}}` - Fecha/hora
- `{{interval}}` - Timeframe

---

## Ejemplo de Alerta Completa

**Condición:** RSI > 70
**Mensaje:**
```
🚨 SOBRECOMPRA

Activo: {{ticker}}
Precio: {{close}}
RSI: > 70

⚠️ Posible reversión bajista
⏰ {{time}}
```

---

## Notas Importantes

1. TradingView requiere cuenta Pro o superior para webhooks
2. Las alertas se envían en tiempo real
3. Puedes crear múltiples alertas con diferentes condiciones
4. El mensaje puede personalizarse completamente

---

## Próximos Pasos

1. [ ] Configurar URL en TradingView
2. [ ] Crear primera alerta de prueba
3. [ ] Verificar recepción en @aidesing_alerts
4. [ ] Crear alertas para múltiples activos

---

## Soporte

Si tienes problemas con la configuración, envíame:
- Screenshot de la configuración
- Mensaje de error (si hay)
- Tipo de cuenta (Free/Pro/Pro+/Premium)