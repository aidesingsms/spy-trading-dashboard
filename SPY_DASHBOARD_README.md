
# SPY Trading Dashboard - TradingView Integration

## Overview
Interactive dashboard with real-time TradingView data for SPY analysis and trading signals.

## Features
- Real-time price updates from TradingView
- Live candlestick chart with indicators (RSI, MACD, MA)
- Support/Resistance levels
- CALL/PUT entry signals
- Technical indicators
- Probability analysis

## TradingView Integration

### Method 1: TradingView Widget (Recommended)
The dashboard uses TradingView's official widget for charts:
```javascript
new TradingView.widget({
    "symbol": "AMEX:SPY",
    "interval": "5",
    "timezone": "America/New_York",
    "theme": "dark",
    "studies": ["RSI@tv-basicstudies", "MACD@tv-basicstudies"]
});
```

### Method 2: WebSocket Connection
For real-time price data, the dashboard attempts to connect to TradingView's WebSocket:
- WebSocket URL: `wss://data.tradingview.com/socket.io/websocket`
- Subscribe to symbols: `AMEX:SPY`
- Receive real-time quotes

### Method 3: REST API Fallback
If WebSocket fails, uses simulated data with realistic price movements.

## Data Sources

### Real-time Data
- **Primary**: TradingView WebSocket
- **Secondary**: TradingView Widget
- **Fallback**: Simulated data

### Historical Data
- TradingView chart provides historical candles
- Indicators calculated on-the-fly

## Signals Configuration

### CALL Signals (LONG)
1. **Breakout Signal**: Price breaks above resistance
2. **Bounce Signal**: Price bounces off support

### PUT Signals (SHORT)
1. **Breakdown Signal**: Price breaks below support
2. **Rejection Signal**: Price rejected at resistance

## Alert System

### Webhook Integration
```json
{
  "symbol": "SPY",
  "signal": "CALL",
  "entry": 736.50,
  "stop": 734.00,
  "target": 740.00,
  "timestamp": "2026-06-30T02:30:00Z"
}
```

### Telegram Alerts
- Sent to @aidesing_alerts
- Real-time notifications
- Entry/Exit signals

## Usage

### Local Development
```bash
# Start local server
python3 -m http.server 8080

# Open browser
open http://localhost:8080/spy_dashboard.html
```

### Production Deployment
1. Upload to web server
2. Configure SSL (HTTPS required for TradingView)
3. Set up webhook endpoints

## Configuration

### TradingView Settings
```javascript
const config = {
    symbol: "AMEX:SPY",
    interval: "5",        // 5-minute candles
    timezone: "America/New_York",
    theme: "dark",
    studies: ["RSI", "MACD", "Bollinger"]
};
```

### Signal Thresholds
```javascript
const signals = {
    call: {
        breakout: 736.50,
        bounce: 733.00
    },
    put: {
        breakdown: 731.50,
        rejection: 735.00
    }
};
```

## API Endpoints

### Get Current Price
```
GET https://quote-api.tradingview.com/watchlist/news/headlines
```

### WebSocket Connection
```
wss://data.tradingview.com/socket.io/websocket
```

## Troubleshooting

### Chart Not Loading
- Check internet connection
- Verify TradingView is accessible
- Check browser console for errors

### Price Not Updating
- WebSocket connection may be blocked
- Fallback to simulated data
- Check firewall settings

### Indicators Not Showing
- Verify studies configuration
- Check TradingView widget loaded
- Refresh page

## Security Notes

- TradingView API requires proper authentication for production
- WebSocket connections may be blocked by CORS
- Use proxy server if needed

## Updates

### Version 1.0 (2026-06-30)
- Initial release
- TradingView widget integration
- Basic signals
- Simulated data fallback

### Planned Features
- Multi-asset support (QQQ, TSLA, NVDA)
- Options chain integration
- Portfolio tracking
- Advanced risk management

## Support

For issues or questions:
- Check TradingView documentation
- Review browser console logs
- Verify network connectivity

## Disclaimer

This dashboard is for educational purposes only. Not financial advice. Always do your own research and manage risk appropriately.
