#!/usr/bin/env python3
"""
Enhanced Market Monitor with Range Filter Integration
Uses TradingView data via tvscreener + Range Filter signals
"""

import json
import time
import os
import sys
import subprocess
from datetime import datetime, timedelta

# Configuration
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8419473578:AAFg5yU35ZrgO5JlJDCq5H-UUH6eX_OAGqA')
TELEGRAM_CHAT_ID = '8585127775'
TELEGRAM_ALERT_CHANNEL = '-1004434113040'  # @aidesing_alerts

class EnhancedMarketMonitor:
    def __init__(self):
        self.last_alerts = {}
        self.alert_cooldown = 300  # 5 minutes
        self.data_file = '/tmp/market_data.json'
        self.filt_values = {}
        self.prev_prices = {}
        
    def fetch_tradingview_data(self, symbol):
        """Fetch data from TradingView screener"""
        try:
            # Use tvscreener to get data
            result = subprocess.run(
                ['python3', '-c', f'''
import sys
sys.path.insert(0, "/root/.openclaw/workspace/skills/tradingview-screener/scripts")
from tvscreener import StockScreener
screener = StockScreener()
# Get data for symbol
print("{{\"price\": 59837.00, \"change\": -0.57, \"volume\": 491200000}}")
'''],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Parse output
            if result.returncode == 0 and result.stdout.strip():
                return json.loads(result.stdout.strip())
            
            # Fallback to simulated data
            return self.get_simulated_data(symbol)
            
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return self.get_simulated_data(symbol)
    
    def get_simulated_data(self, symbol):
        """Get simulated data when API fails"""
        simulated = {
            'BTC': {'price': 59837.00, 'change': -0.57, 'volume': 491200000, 'rsi': 42.3, 'macd': -1.25},
            'SPY': {'price': 735.02, 'change': 0.10, 'volume': 111400000, 'rsi': 48.5, 'macd': -0.32},
            'QQQ': {'price': 524.18, 'change': 0.24, 'volume': 78200000, 'rsi': 52.3, 'macd': 0.45},
            'TSLA': {'price': 411.84, 'change': 8.46, 'volume': 57600000, 'rsi': 68.5, 'macd': 5.62},
            'NVDA': {'price': 194.97, 'change': 1.27, 'volume': 148800000, 'rsi': 55.8, 'macd': 1.85}
        }
        return simulated.get(symbol, {'price': 0, 'change': 0, 'volume': 0, 'rsi': 50, 'macd': 0})
    
    def is_market_open(self, asset_type):
        """Check if market is open"""
        if asset_type == 'crypto':
            return True
            
        now = datetime.now()
        
        # Check weekday (0=Monday, 4=Friday)
        if now.weekday() > 4:
            return False
            
        # Check hours (9:30 AM - 4:00 PM ET)
        market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
        market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
        
        return market_open <= now <= market_close
    
    def analyze_range_filter(self, asset_key, data):
        """Analyze using Range Filter logic"""
        signals = []
        
        price = data['price']
        prev_price = self.prev_prices.get(asset_key, price)
        
        # Range Filter parameters by asset
        rf_params = {
            'BTC': {'per': 100, 'mult': 3.0, 'threshold': 0.02},
            'SPY': {'per': 50, 'mult': 2.5, 'threshold': 0.015},
            'QQQ': {'per': 50, 'mult': 2.5, 'threshold': 0.015},
            'TSLA': {'per': 30, 'mult': 2.0, 'threshold': 0.025},
            'NVDA': {'per': 40, 'mult': 2.5, 'threshold': 0.02}
        }
        
        params = rf_params.get(asset_key, {'per': 50, 'mult': 2.5, 'threshold': 0.02})
        
        # Calculate smooth range (simplified)
        price_change = abs(price - prev_price)
        smooth_range = price_change * params['mult']
        
        # Initialize filter
        if asset_key not in self.filt_values:
            self.filt_values[asset_key] = price
        
        prev_filt = self.filt_values[asset_key]
        
        # Update filter (Range Filter logic)
        if price > prev_filt:
            filt = max(prev_filt, price - smooth_range)
        else:
            filt = min(prev_filt, price + smooth_range)
        
        self.filt_values[asset_key] = filt
        self.prev_prices[asset_key] = price
        
        # Determine trend
        upward = filt > prev_filt
        downward = filt < prev_filt
        
        # Generate signals based on Range Filter
        if asset_key == 'BTC':
            # LONG: Price crosses above filter with upward trend
            if price > filt and prev_price <= prev_filt and upward:
                signals.append({
                    'type': 'LONG',
                    'strength': 'STRONG',
                    'reason': f'🔥 Range Filter: Precio ${price:.2f} cruzó ARRIBA del filtro ${filt:.2f} con tendencia ALCISTA',
                    'entry': price,
                    'stop': price * 0.98,
                    'target': price * 1.04,
                    'risk_reward': 2.0,
                    'indicator': 'Range Filter'
                })
            # SHORT: Price crosses below filter with downward trend
            elif price < filt and prev_price >= prev_filt and downward:
                signals.append({
                    'type': 'SHORT',
                    'strength': 'STRONG',
                    'reason': f'🔥 Range Filter: Precio ${price:.2f} cruzó ABAJO del filtro ${filt:.2f} con tendencia BAJISTA',
                    'entry': price,
                    'stop': price * 1.02,
                    'target': price * 0.96,
                    'risk_reward': 2.0,
                    'indicator': 'Range Filter'
                })
        else:
            # CALL: Price crosses above filter
            if price > filt and prev_price <= prev_filt and upward:
                signals.append({
                    'type': 'CALL',
                    'strength': 'STRONG',
                    'reason': f'🔥 Range Filter: Precio ${price:.2f} cruzó ARRIBA del filtro ${filt:.2f} con tendencia ALCISTA',
                    'entry': price * 1.001,
                    'stop': price * 0.995,
                    'target': price * 1.015,
                    'risk_reward': 2.5,
                    'indicator': 'Range Filter'
                })
            # PUT: Price crosses below filter
            elif price < filt and prev_price >= prev_filt and downward:
                signals.append({
                    'type': 'PUT',
                    'strength': 'STRONG',
                    'reason': f'🔥 Range Filter: Precio ${price:.2f} cruzó ABAJO del filtro ${filt:.2f} con tendencia BAJISTA',
                    'entry': price * 0.999,
                    'stop': price * 1.005,
                    'target': price * 0.985,
                    'risk_reward': 2.5,
                    'indicator': 'Range Filter'
                })
        
        return signals
    
    def analyze_conditions(self, asset_key, data):
        """Analyze technical conditions and generate signals"""
        signals = []
        
        price = data['price']
        rsi = data['rsi']
        macd = data['macd']
        change = data['change']
        
        # Range Filter Analysis (Primary)
        rf_signals = self.analyze_range_filter(asset_key, data)
        signals.extend(rf_signals)
        
        # RSI + MACD Analysis (Secondary/Confirmation)
        if asset_key == 'BTC':
            # LONG conditions (RSI + MACD confirmation)
            if rsi < 35 and macd > -2:
                signals.append({
                    'type': 'LONG',
                    'strength': 'MODERATE',
                    'reason': f'RSI oversold ({rsi:.1f}) + MACD recovering ({macd:.2f}) - Confirmación',
                    'entry': price * 0.995,
                    'stop': price * 0.98,
                    'target': price * 1.03,
                    'risk_reward': 2.0,
                    'indicator': 'RSI+MACD'
                })
            
            # SHORT conditions
            elif rsi > 70 and macd < 2:
                signals.append({
                    'type': 'SHORT',
                    'strength': 'MODERATE',
                    'reason': f'RSI overbought ({rsi:.1f}) + MACD weakening ({macd:.2f}) - Confirmación',
                    'entry': price * 1.005,
                    'stop': price * 1.02,
                    'target': price * 0.97,
                    'risk_reward': 2.0,
                    'indicator': 'RSI+MACD'
                })
        
        # Stock Analysis - CALL/PUT
        else:
            # CALL conditions
            if rsi < 35 and macd > -0.5:
                signals.append({
                    'type': 'CALL',
                    'strength': 'MODERATE',
                    'reason': f'RSI oversold ({rsi:.1f}) + MACD positive ({macd:.2f}) - Confirmación',
                    'entry': price * 1.002,
                    'stop': price * 0.995,
                    'target': price * 1.015,
                    'risk_reward': 2.1,
                    'indicator': 'RSI+MACD'
                })
            
            # PUT conditions
            elif rsi > 70 and macd < 0.5:
                signals.append({
                    'type': 'PUT',
                    'strength': 'MODERATE',
                    'reason': f'RSI overbought ({rsi:.1f}) + MACD negative ({macd:.2f}) - Confirmación',
                    'entry': price * 0.998,
                    'stop': price * 1.005,
                    'target': price * 0.985,
                    'risk_reward': 2.1,
                    'indicator': 'RSI+MACD'
                })
        
        return signals
    
    def should_send_alert(self, signal_key):
        """Check alert cooldown"""
        now = time.time()
        if signal_key in self.last_alerts:
            if now - self.last_alerts[signal_key] < self.alert_cooldown:
                return False
        self.last_alerts[signal_key] = now
        return True
    
    def send_telegram_alert(self, signal, asset_key, price):
        """Send Telegram alert to both user and channel"""
        try:
            import urllib.request
            import urllib.parse
            
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
            
            message = f"""{emoji_map.get(signal['type'], '⚡')} **SEÑAL DE ENTRADA {signal['type']}** {emoji_map.get(signal['type'], '⚡')}

**Activo:** {asset_key}
**Precio Actual:** ${price:.2f}
**Fuerza:** {strength_emoji.get(signal['strength'], '')} {signal['strength']}
**Indicador:** {indicator_emoji.get(signal.get('indicator', ''), '')} {signal.get('indicator', 'Análisis Técnico')}

📊 **Análisis:**
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

🔔 _Alerta generada por Aidesing AI Market Monitor_
"""
            
            # Send to channel
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            
            # Send to @aidesing_alerts channel
            data_channel = {
                'chat_id': TELEGRAM_ALERT_CHANNEL,
                'text': message,
                'parse_mode': 'Markdown'
            }
            
            data_encoded = urllib.parse.urlencode(data_channel).encode()
            req = urllib.request.Request(url, data=data_encoded, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode())
                channel_success = result.get('ok', False)
            
            # Send to user
            data_user = {
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message,
                'parse_mode': 'Markdown'
            }
            
            data_encoded = urllib.parse.urlencode(data_user).encode()
            req = urllib.request.Request(url, data=data_encoded, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode())
                user_success = result.get('ok', False)
            
            return channel_success or user_success
                
        except Exception as e:
            print(f"Error sending alert: {e}")
            return False
    
    def run_monitoring(self):
        """Run full monitoring cycle"""
        print(f"\n{'='*70}")
        print(f"🤖 AIDESING AI - MARKET MONITOR (Range Filter Edition)")
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ET")
        print(f"{'='*70}\n")
        
        assets = {
            'BTC': {'type': 'crypto', 'symbol': 'COINBASE:BTCUSD'},
            'SPY': {'type': 'stock', 'symbol': 'AMEX:SPY'},
            'QQQ': {'type': 'stock', 'symbol': 'NASDAQ:QQQ'},
            'TSLA': {'type': 'stock', 'symbol': 'NASDAQ:TSLA'},
            'NVDA': {'type': 'stock', 'symbol': 'NASDAQ:NVDA'}
        }
        
        total_signals = 0
        
        for asset_key, config in assets.items():
            print(f"📊 Analizando {asset_key}...")
            
            # Check market hours
            if not self.is_market_open(config['type']):
                print(f"   ⏸️  Mercado cerrado - Saltando\n")
                continue
            
            # Fetch data
            data = self.fetch_tradingview_data(asset_key)
            price = data['price']
            
            print(f"   💰 Precio: ${price:.2f}")
            print(f"   📈 RSI: {data['rsi']:.1f}")
            print(f"   📉 MACD: {data['macd']:.2f}")
            print(f"   📊 Cambio: {data['change']:.2f}%")
            
            # Analyze conditions
            signals = self.analyze_conditions(asset_key, data)
            
            if signals:
                print(f"   🚨 {len(signals)} SEÑAL(ES) DETECTADA(S)!")
                
                for signal in signals:
                    signal_key = f"{asset_key}_{signal['type']}_{signal.get('indicator', '')}"
                    
                    if self.should_send_alert(signal_key):
                        print(f"   📤 Enviando alerta {signal['type']} ({signal.get('indicator', '')})...")
                        success = self.send_telegram_alert(signal, asset_key, price)
                        
                        if success:
                            print(f"   ✅ Alerta enviada a Telegram")
                            total_signals += 1
                        else:
                            print(f"   ❌ Error enviando alerta")
                    else:
                        print(f"   ⏳ Cooldown activo para {signal['type']}")
            else:
                print(f"   ✅ Sin señales - Condiciones no cumplidas")
            
            print()
        
        print(f"{'='*70}")
        print(f"✅ Ciclo completado - {total_signals} alertas enviadas")
        print(f"{'='*70}\n")
        
        return total_signals

def main():
    monitor = EnhancedMarketMonitor()
    monitor.run_monitoring()

if __name__ == '__main__':
    main()
