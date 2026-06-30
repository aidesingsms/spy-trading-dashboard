#!/usr/bin/env python3
"""
Test Range Filter Alert - Simulates a signal to test the system
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime

# Configuration
TELEGRAM_BOT_TOKEN = "8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA"
TELEGRAM_CHAT_ID = "8585127775"
TELEGRAM_ALERT_CHANNEL = "-1004434113040"  # @aidesing_alerts

def send_range_filter_test_alert():
    """Send a test alert simulating Range Filter signal"""
    
    # Test signal for BTC LONG using Range Filter
    signal = {
        'type': 'LONG',
        'asset': 'BTC',
        'strength': 'STRONG',
        'indicator': 'Range Filter',
        'reason': '🔥 Range Filter: Precio $59,837.00 cruzó ARRIBA del filtro $59,500.00 con tendencia ALCISTA\n\n📊 Confirmación técnica:\n• Filtro anterior: $59,200.00\n• Precio anterior: $59,100.00\n• Tendencia: ALCISTA (3 velas consecutivas)\n• Smooth Range: $337.50',
        'entry': 59837.00,
        'stop': 58640.26,
        'target': 62230.48,
        'risk_reward': 2.0
    }
    
    price = 59837.00
    
    emoji_map = {
        'LONG': '🟢📈',
        'SHORT': '🔴📉',
        'CALL': '🟢📞',
        'PUT': '🔴📞'
    }
    
    strength_emoji = {
        'STRONG': '💪',
        'MODERATE': '⚡',
        'WEAK': '👀'
    }
    
    indicator_emoji = {
        'Range Filter': '🎯',
        'RSI+MACD': '📊'
    }
    
    message = f"""🧪 **SEÑAL DE PRUEBA - RANGE FILTER** 🧪

{emoji_map.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji_map.get(signal['type'], '⚡')}

**Activo:** {signal['asset']}
**Precio Actual:** ${price:.2f}
**Fuerza:** {strength_emoji.get(signal['strength'], '')} {signal['strength']}
**Indicador:** {indicator_emoji.get(signal.get('indicator', ''), '')} {signal.get('indicator', 'Análisis Técnico')}

📊 **Análisis Range Filter:**
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
• No operar en noticias

🔔 _Esta es una señal de PRUEBA del sistema Aidesing AI Range Filter_
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
            if channel_success:
                print("✅ Alerta de prueba enviada a @aidesing_alerts")
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
            if user_success:
                print("✅ Alerta de prueba enviada a usuario")
    except Exception as e:
        print(f"Error enviando a usuario: {e}")
        user_success = False
    
    if channel_success or user_success:
        print("\n✅ Alerta de prueba Range Filter completada")
        return True
    else:
        print("\n❌ Error enviando alerta de prueba")
        return False

def send_range_filter_put_test():
    """Send a test PUT alert using Range Filter"""
    
    # Test signal for SPY PUT using Range Filter
    signal = {
        'type': 'PUT',
        'asset': 'SPY',
        'strength': 'STRONG',
        'indicator': 'Range Filter',
        'reason': '🔥 Range Filter: Precio $735.02 cruzó ABAJO del filtro $738.50 con tendencia BAJISTA\n\n📊 Confirmación técnica:\n• Filtro anterior: $740.20\n• Precio anterior: $741.00\n• Tendencia: BAJISTA (2 velas consecutivas)\n• Smooth Range: $3.75',
        'entry': 734.27,
        'stop': 738.69,
        'target': 724.40,
        'risk_reward': 2.5
    }
    
    price = 735.02
    
    emoji_map = {
        'LONG': '🟢📈',
        'SHORT': '🔴📉',
        'CALL': '🟢📞',
        'PUT': '🔴📞'
    }
    
    strength_emoji = {
        'STRONG': '💪',
        'MODERATE': '⚡',
        'WEAK': '👀'
    }
    
    indicator_emoji = {
        'Range Filter': '🎯',
        'RSI+MACD': '📊'
    }
    
    message = f"""🧪 **SEÑAL DE PRUEBA - RANGE FILTER** 🧪

{emoji_map.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji_map.get(signal['type'], '⚡')}

**Activo:** {signal['asset']}
**Precio Actual:** ${price:.2f}
**Fuerza:** {strength_emoji.get(signal['strength'], '')} {signal['strength']}
**Indicador:** {indicator_emoji.get(signal.get('indicator', ''), '')} {signal.get('indicator', 'Análisis Técnico')}

📊 **Análisis Range Filter:**
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
• No operar en noticias

🔔 _Esta es una señal de PRUEBA del sistema Aidesing AI Range Filter_
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
            if channel_success:
                print("✅ Alerta PUT de prueba enviada a @aidesing_alerts")
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
            if user_success:
                print("✅ Alerta PUT de prueba enviada a usuario")
    except Exception as e:
        print(f"Error enviando a usuario: {e}")
        user_success = False
    
    if channel_success or user_success:
        print("\n✅ Alerta PUT de prueba Range Filter completada")
        return True
    else:
        print("\n❌ Error enviando alerta PUT de prueba")
        return False

if __name__ == '__main__':
    print("🚀 Enviando señales de prueba Range Filter...")
    print()
    
    # Send BTC LONG test alert
    print("📤 Enviando alerta BTC LONG (Range Filter)...")
    send_range_filter_test_alert()
    
    print()
    
    # Send SPY PUT test alert
    print("📤 Enviando alerta SPY PUT (Range Filter)...")
    send_range_filter_put_test()
    
    print()
    print("✅ Señales de prueba Range Filter completadas")
