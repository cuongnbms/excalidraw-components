# Excalidraw Components

Reusable Excalidraw component library for system design diagrams.

## Components

### System Design (`system-design/`)

| File | Components |
|------|------------|
| `client.excalidraw` | User, Mobile, Laptop, Admin, Tablet, Desktop |
| `database.excalidraw` | Database, Primary/Replica DB, MongoDB, Redis, PostgreSQL |
| `gateway.excalidraw` | API Gateway, Authentication, Rate Limiting |
| `loadbalancer.excalidraw` | Load Balancer variants |
| `queue.excalidraw` | Message Queue, Kafka, RabbitMQ |
| `vault.excalidraw` | Vault, Key, Lock, Secrets, Certificate, Shield |

## Usage

1. Open any `.excalidraw` file in [Excalidraw](https://excalidraw.com)
2. Select components you need
3. Copy and paste into your diagram

## Structure

```
system-design/
  client.excalidraw      # Client-side: users, devices
  database.excalidraw    # Data storage: SQL, NoSQL, cache
  gateway.excalidraw     # API gateways, auth
  loadbalancer.excalidraw # Traffic distribution
  queue.excalidraw       # Message queues, streaming
  vault.excalidraw       # Security: secrets, keys, certs
```

## Style Guide

- **Stroke**: `#1e1e1e`, width 2
- **Fill**: Solid, pastel colors
- **Labels**: Font size 14-16, centered
- **Roughness**: 1 (hand-drawn style)
