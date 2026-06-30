#!/usr/bin/env python3
"""
Market Monitor - Analyzes technical indicators and sends alerts
Runs every 5 minutes during market hours
"""

import json
import time
import os
import sys
from datetime import datetime, timedelta

# Configuration
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA')
TELEGRAM_CHAT_ID = '8585127775'

# Asset configurations
ASSETS = {
    'BTC': {
        'symbol': 'COINBASE:BTCUSD',
        'type': 'crypto',
        'market_hours': '24/7',
        'timeframes': ['5', '15', '60'],
        'indicators': {
            'rsi_overbought': 70,
            'rsi_oversold': 30,
            'rsi_neutral_high': 60,
            'rsi_neutral_low': 40,
        },
        'levels': {
            'long_entry': 59100,
            'long_stop': 58400,
            'long_target': 61000,
            'short_entry': 60500,
            'short_stop': 61200,
            'short_target': 58500,
        }
    },
    'SPY': {
        'symbol': 'AMEX:SPY',
        'type': 'stock',
        'market_hours': '09:30-16:00',
        'timeframes': ['5', '15', '60'],
        'indicators': {
            'rsi_overbought': 70,
            'rsi_oversold': 30,
            'rsi_neutral_high': 60,
            'rsi_neutral_low': 40,
        },
        'levels': {
            'call_entry': 736.50,
            'call_stop': 734.00,
            'call_target': 740.00,
            'put_entry': 731.50,
            'put_stop': 734.00,
            'put_target': 728.00,
        }
    },
    'QQQ': {
        'symbol': 'NASDAQ:QQQ',
        'type': 'stock',
        'market_hours': '09:30-16:00',
        'timeframes': ['5', '15', '60'],
        'indicators': {
            'rsi_overbought': 70,
            'rsi_oversold': 30,
        },
        'levels': {
            'call_entry': 526.50,
            'call_stop': 524.00,
            'call_target': 530.00,
            'put_entry': 521.50,
            'put_stop': 524.00,
            'put_target': 518.00,
        }
    },
    'TSLA': {
        'symbol': 'NASDAQ:TSLA',
        'type': 'stock',
        'market_hours': '09:30-16:00',
        'timeframes': ['5', '15', '60'],
        'indicators': {
            'rsi_overbought': 75,
            'rsi_oversold': 25,
        },
        'levels': {
            'call_entry': 415.00,
            'call_stop': 408.00,
            'call_target': 425.00,
            'put_entry': 418.00,
            'put_stop': 425.00,
            'put_target': 400.00,
        }
    },
    'NVDA': {
        'symbol': 'NASDAQ:NVDA',
        'type': 'stock',
        'market_hours': '09:30-16:00',
        'timeframes': ['5', '15', '60'],
        'indicators': {
            'rsi_overbought': 70,
            'rsi_oversold': 30,
        },
        'levels': {
            'call_entry': 197.00,
            'call_stop': 194.00,
            'call_target': 202.00,
            'put_entry': 191.00,
            'put_stop': 194.00,
            'put_target': 187.00,
        }
    }
}

class MarketMonitor:
    def __init__(self):
        self.last_alerts = {}
        self.alert_cooldown = 300  # 5 minutes between same alerts
        
    def is_market_open(self, asset_type):
        """Check if market is open for the asset type"""
        if asset_type == 'crypto':
            return True
            
        # Stock market hours: 9:30 AM - 4:00 PM ET
        now = datetime.now()
        et_time = now  # Assuming server is on ET
        
        market_open = et_time.replace(hour=9, minute=30, second=0, microsecond=0)
        market_close = et_time.replace(hour=16, minute=0, second=0, microsecond=0)
        
        # Check if weekday (0=Monday, 4=Friday)
        if et_time.weekday() > 4:
            return False
            
        return market_open <= et_time <= market_close
    
    def calculate_rsi(self, prices, period=14):
        """Calculate RSI from price list"""
        if len(prices) < period + 1:
            return 50  # Neutral if not enough data
            
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
            
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate_sma(self, prices, period):
        """Calculate Simple Moving Average"""
        if len(prices) < period:
            return sum(prices) / len(prices)
        return sum(prices[-period:]) / period
    
    def calculate_macd(self, prices):
        """Calculate MACD"""
        ema12 = self.calculate_ema(prices, 12)
        ema26 = self.calculate_ema(prices, 26)
        macd = ema12 - ema26
        return macd
    
    def calculate_ema(self, prices, period):
        """Calculate Exponential Moving Average"""
        if len(prices) < period:
            return sum(prices) / len(prices)
            
        multiplier = 2 / (period + 1)
        ema = sum(prices[:period]) / period
        
        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema
            
        return ema
    
    def analyze_asset(self, asset_key, current_price, prices_history):
        """Analyze asset and generate signals"""
        asset = ASSETS[asset_key]
        signals = []
        
        # Calculate indicators
        rsi = self.calculate_rsi(prices_history)
        sma50 = self.calculate_sma(prices_history, 50)
        sma200 = self.calculate_sma(prices_history, 200)
        macd = self.calculate_macd(prices_history)
        
        # Determine trend
        trend = 'neutral'
        if current_price > sma50 and current_price > sma200:
            trend = 'bullish'
        elif current_price < sma50 and current_price < sma200:
            trend = 'bearish'
        
        # Generate signals based on asset type
        if asset['type'] == 'crypto':
            # BTC signals - LONG/SHORT
            if rsi < asset['indicators']['rsi_oversold'] and trend == 'bullish':
                signals.append({
                    'type': 'LONG',
                    'asset': asset_key,
                    'strength': 'strong',
                    'reason': f'RSI oversold ({rsi:.1f}) + Bullish trend',
                    'entry': asset['levels']['long_entry'],
                    'stop': asset['levels']['long_stop'],
                    'target': asset['levels']['long_target'],
                    'risk_reward': 2.7
                })
            elif rsi > asset['indicators']['rsi_overbought'] and trend == 'bearish':
                signals.append({
                    'type': 'SHORT',
                    'asset': asset_key,
                    'strength': 'strong',
                    'reason': f'RSI overbought ({rsi:.1f}) + Bearish trend',
                    'entry': asset['levels']['short_entry'],
                    'stop': asset['levels']['short_stop'],
                    'target': asset['levels']['short_target'],
                    'risk_reward': 2.9
                })
        else:
            # Stock signals - CALL/PUT
            if rsi < asset['indicators']['rsi_oversold'] and macd > 0:
                signals.append({
                    'type': 'CALL',
                    'asset': asset_key,
                    'strength': 'strong',
                    'reason': f'RSI oversold ({rsi:.1f}) + MACD positive ({macd:.2f})',
                    'entry': asset['levels']['call_entry'],
                    'stop': asset['levels']['call_stop'],
                    'target': asset['levels']['call_target'],
                    'risk_reward': 1.6
                })
            elif rsi > asset['indicators']['rsi_overbought'] and macd < 0:
                signals.append({
                    'type': 'PUT',
                    'asset': asset_key,
                    'strength': 'strong',
                    'reason': f'RSI overbought ({rsi:.1f}) + MACD negative ({macd:.2f})',
                    'entry': asset['levels']['put_entry'],
                    'stop': asset['levels']['put_stop'],
                    'target': asset['levels']['put_target'],
                    'risk_reward': 1.4
                })
        
        return {
            'asset': asset_key,
            'price': current_price,
            'rsi': rsi,
            'sma50': sma50,
            'sma200': sma200,
            'macd': macd,
            'trend': trend,
            'signals': signals
        }
    
    def should_send_alert(self, signal_key):
        """Check if enough time has passed since last alert"""
        now = time.time()
        if signal_key in self.last_alerts:
            if now - self.last_alerts[signal_key] < self.alert_cooldown:
                return False
        self.last_alerts[signal_key] = now
        return True
    
    def send_telegram_alert(self, signal):
        """Send alert via Telegram"""
        import urllib.request
        import urllib.parse
        
        emoji = {
            'LONG': '🟢📈',
            'SHORT': '🔴📉',
            'CALL': '🟢📞',
            'PUT': '🔴📞'
        }
        
        message = f"""
{emoji.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji.get(signal['type'], '⚡')}

**Activo:** {signal['asset']}
**Fuerza:** {signal['strength'].upper()}

📊 **Análisis:**
{signal['reason']}

💰 **Niveles:**
• Entrada: ${signal['entry']:.2f}
• Stop Loss: ${signal['stop']:.2f}
• Target: ${signal['target']:.2f}
• R/R: 1:{signal['risk_reward']:.1f}

⏰ **Hora:** {datetime.now().strftime('%H:%M:%S')} ET

⚠️ **Gestión de Riesgo:**
• Máximo 3% del portafolio
• Stop loss obligatorio
• No operar sin confirmación

🔔 Alerta generada por Aidesing AI Monitor
"""
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        
        try:
            data_encoded = urllib.parse.urlencode(data).encode()
            req = urllib.request.Request(url, data=data_encoded, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode())
                return result.get('ok', False)
        except Exception as e:
            print(f"Error sending Telegram alert: {e}")
            return False
    
    def run_monitoring_cycle(self):
        """Run one monitoring cycle"""
        print(f"\n{'='*60}")
        print(f"Market Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ET")
        print(f"{'='*60}\n")
        
        # Simulated prices (in production, fetch from API)
        simulated_prices = {
            'BTC': 59837.00,
            'SPY': 735.02,
            'QQQ': 524.18,
            'TSLA': 411.84,
            'NVDA': 194.97
        }
        
        # Simulated price history (in production, fetch from API)
        import random
        for asset_key, current_price in simulated_prices.items():
            asset = ASSETS[asset_key]
            
            # Check market hours
            if not self.is_market_open(asset['type']):
                print(f"⏸️  {asset_key}: Market closed, skipping...")
                continue
            
            # Generate simulated price history
            prices_history = []
            price = current_price
            for _ in range(200):
                prices_history.append(price)
                price = price * (1 + random.uniform(-0.002, 0.002))
            prices_history.reverse()
            
            # Analyze asset
            analysis = self.analyze_asset(asset_key, current_price, prices_history)
            
            print(f"📊 {asset_key} Analysis:")
            print(f"   Price: ${current_price:.2f}")
            print(f"   RSI: {analysis['rsi']:.1f}")
            print(f"   Trend: {analysis['trend']}")
            print(f"   MACD: {analysis['macd']:.2f}")
            
            # Check for signals
            if analysis['signals']:
                for signal in analysis['signals']:
                    signal_key = f"{signal['asset']}_{signal['type']}"
                    
                    if self.should_send_alert(signal_key):
                        print(f"   🚨 SIGNAL: {signal['type']} - {signal['reason']}")
                        success = self.send_telegram_alert(signal)
                        if success:
                            print(f"   ✅ Alert sent to Telegram")
                        else:
                            print(f"   ❌ Failed to send alert")
                    else:
                        print(f"   ⏳ Signal cooldown active for {signal['type']}")
            else:
                print(f"   ✅ No signals - conditions not met")
            
            print()

def main():
    """Main function"""
    monitor = MarketMonitor()
    
    # Run monitoring cycle
    monitor.run_monitoring_cycle()
    
    print(f"\n{'='*60}")
    print("Monitoring cycle complete")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
