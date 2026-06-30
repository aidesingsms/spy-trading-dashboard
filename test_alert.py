#!/usr/bin/env python3
"""
Test Alert - Sends a test signal to verify the notification system
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime

# Configuration
TELEGRAM_BOT_TOKEN = "8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA"
TELEGRAM_CHAT_ID = "8585127775"
TELEGRAM_ALERT_CHANNEL = "-1004434113040"  # @aidesing_alerts

def send_test_alert():
    """Send a test alert"""
    
    # Test signal for BTC LONG
    signal = {
        'type': 'LONG',
        'asset': 'BTC',
        'strength': 'STRONG',
        'reason': 'RSI oversold (28.5) + MACD recovering (-0.85) + Bounce from support $59,100',
        'entry': 59100.00,
        'stop': 58400.00,
        'target': 61000.00,
        'risk_reward': 2.7
    }
    
    price = 59837.00
    
    emoji_map = {
        'LONG': '🟢📈',
        'SHORT': '🔴📉',
        'CALL': '🟢📞',
        'PUT': '🔴📞'
    }
    
    message = f"""🧪 **SEÑAL DE PRUEBA** 🧪

{emoji_map.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji_map.get(signal['type'], '⚡')}

**Activo:** {signal['asset']}
**Precio Actual:** ${price:.2f}
**Fuerza:** 💪 {signal['strength']}

📊 **Análisis Técnico:**
{signal['reason']}

💰 **Niveles de Entrada:**
• 🎯 Entrada: ${signal['entry']:.2f}
• 🛑 Stop Loss: ${signal['stop']:.2f}
• ✅ Target: ${signal['target']:.2f}
• 📈 R/R: 1:{signal['risk_reward']:.1f}

⏰ **Hora:** {datetime.now().strftime('%H:%M:%S')} ET
📅 **Fecha:** {datetime.now().strftime('%Y-%m-%d')}

⚠️ **Gestión de Riesgo:**
• Máximo 3% del portafolio por trade
• Stop loss obligatorio
• Confirmar con volumen
• No operar sin confirmación

🔔 _Esta es una señal de PRUEBA del sistema Aidesing AI Market Monitor_
"""
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Send to channel
    data_channel = {
        'chat_id': TELEGRAM_ALERT_CHANNEL,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        data_encoded = urllib.parse.urlencode(data_channel).encode()
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            channel_success = result.get('ok', False)
    except Exception as e:
        print(f"Error enviando a canal: {e}")
        channel_success = False
    
    # Send to user
    data_user = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        data_encoded = urllib.parse.urlencode(data_user).encode()
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            user_success = result.get('ok', False)
    except Exception as e:
        print(f"Error enviando a usuario: {e}")
        user_success = False
    
    if channel_success or user_success:
        print("✅ Alerta de prueba enviada exitosamente")
        return True
    else:
        print("❌ Error enviando alerta")
        return False

def send_test_stock_alert():
    """Send a test stock alert"""
    
    # Test signal for SPY CALL
    signal = {
        'type': 'CALL',
        'asset': 'SPY',
        'strength': 'MODERATE',
        'reason': 'RSI oversold (32.1) + MACD positive (0.45) + Bounce from SMA 50 ($728.50)',
        'entry': 736.50,
        'stop': 734.00,
        'target': 740.00,
        'risk_reward': 1.6
    }
    
    price = 735.02
    
    emoji_map = {
        'LONG': '🟢📈',
        'SHORT': '🔴📉',
        'CALL': '🟢📞',
        'PUT': '🔴📞'
    }
    
    message = f"""🧪 **SEÑAL DE PRUEBA** 🧪

{emoji_map.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji_map.get(signal['type'], '⚡')}

**Activo:** {signal['asset']}
**Precio Actual:** ${price:.2f}
**Fuerza:** ⚡ {signal['strength']}

📊 **Análisis Técnico:**
{signal['reason']}

💰 **Niveles de Entrada:**
• 🎯 Entrada: ${signal['entry']:.2f}
• 🛑 Stop Loss: ${signal['stop']:.2f}
• ✅ Target: ${signal['target']:.2f}
• 📈 R/R: 1:{signal['risk_reward']:.1f}

⏰ **Hora:** {datetime.now().strftime('%H:%M:%S')} ET
📅 **Fecha:** {datetime.now().strftime('%Y-%m-%d')}

⚠️ **Gestión de Riesgo:**
• Máximo 3% del portafolio por trade
• Stop loss obligatorio
• Confirmar con volumen
• No operar sin confirmación

🔔 _Esta es una señal de PRUEBA del sistema Aidesing AI Market Monitor_
"""
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Send to channel
    data_channel = {
        'chat_id': TELEGRAM_ALERT_CHANNEL,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        data_encoded = urllib.parse.urlencode(data_channel).encode()
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            channel_success = result.get('ok', False)
    except Exception as e:
        print(f"Error enviando a canal: {e}")
        channel_success = False
    
    # Send to user
    data_user = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        data_encoded = urllib.parse.urlencode(data_user).encode()
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            user_success = result.get('ok', False)
    except Exception as e:
        print(f"Error enviando a usuario: {e}")
        user_success = False
    
    if channel_success or user_success:
        print("✅ Alerta de prueba SPY enviada exitosamente")
        return True
    else:
        print("❌ Error enviando alerta")
        return False

if __name__ == '__main__':
    print("🚀 Enviando señales de prueba...")
    print()
    
    # Send BTC test alert
    print("📤 Enviando alerta BTC LONG...")
    send_test_alert()
    
    print()
    
    # Send SPY test alert
    print("📤 Enviando alerta SPY CALL...")
    send_test_stock_alert()
    
    print()
    print("✅ Señales de prueba completadas")
