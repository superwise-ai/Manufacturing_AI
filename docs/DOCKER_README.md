# Docker Setup for Manufacturing AI

This document provides comprehensive instructions for running Manufacturing AI using Docker.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Docker Compose (included with Docker Desktop)
- At least 4GB of available RAM
- At least 2GB of available disk space

## Quick Start

### 1. Environment Configuration

**Required for Superwise AI integration:**

Follow the environment setup steps in the main [README.md](../README.md#setup-steps) to create your `.env` file with Superwise API credentials.

**Quick Reference:**
```bash
# Copy the example file
cp .env.example .env

# Edit with your Superwise API credentials
SUPERWISE_BASE_URL=https://api.superwise.ai/
SUPERWISE_APP_ID=YOUR_SUPERWISE_APP_ID
```

**Note**: The Superwise agent configuration is required for AI features to work properly.

### 2. Using Docker Compose

```bash
# Build and start the application
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

## Docker Commands Reference

### Basic Operations

```bash
# Build the image
docker-compose build

# Start services
docker-compose up

# Start services in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f medinext-ai
```

### Development Commands

```bash
# Rebuild and restart (useful during development)
docker-compose up --build --force-recreate

# Access container shell
docker-compose exec medinext-ai /bin/bash

# View running containers
docker-compose ps

# View resource usage
docker stats
```

### Cleanup Commands

```bash
# Stop and remove containers
docker-compose down

# Stop and remove containers, volumes
docker-compose down --volumes

# Remove all unused containers, images
docker system prune -f

# Remove specific images
docker rmi medinext_ai_medinext-ai
```

## Configuration

### Port Configuration

Default port mapping:
- **Application**: `localhost:8501`

## Production Deployment

### Using Production Compose File

```bash
# Use production configuration
docker-compose -f docker-compose.prod.yml up -d

# Build production image
docker-compose -f docker-compose.prod.yml build

# Stop production services
docker-compose -f docker-compose.prod.yml down
```

### Production Features

The production configuration can include:
- **Nginx reverse proxy** with SSL support
- **Resource limits** and health checks
- **Security headers** and rate limiting
- **Database and cache services** (if needed)

### SSL Configuration

1. Place SSL certificates in `nginx/ssl/`:
   ```
   nginx/ssl/
   ├── cert.pem
   └── key.pem
   ```

2. Uncomment HTTPS configuration in `nginx/nginx.conf`

3. Update `docker-compose.prod.yml` to redirect HTTP to HTTPS

## Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Check what's using port 9000
netstat -ano | findstr :8501  # Windows
lsof -i :8501                  # Linux/Mac

# Change port in docker-compose.yml
ports:
  - "9002:8501"
```

**Container Won't Start:**
```bash
# Check logs
docker-compose logs manufacturing-ai

# Check container status
docker-compose ps

# Rebuild image
docker-compose build --no-cache
```

**Permission Issues:**
```bash
# On Linux/Mac, ensure proper file permissions
chmod -R 755 .

# Or run with sudo (not recommended for production)
sudo docker-compose up
```

**Out of Memory:**
```bash
# Increase Docker memory limit in Docker Desktop settings
# Or add memory limits in docker-compose.yml
deploy:
  resources:
    limits:
      memory: 2G
```

### Debugging

**Access Container Shell:**
```bash
docker-compose exec manufacturing-ai /bin/bash
```

**View Container Logs:**
```bash
docker-compose logs -f manufacturing-ai
```

**Check Container Resources:**
```bash
docker stats manufacturing-ai
```

**Inspect Container:**
```bash
docker inspect manufacturing-ai
```

## Performance Optimization

### Resource Limits

```yaml
deploy:
  resources:
    limits:
      memory: 1G
      cpus: '1.0'
    reservations:
      memory: 512M
      cpus: '0.5'
```

### Volume Mounts

For development, source code is mounted as a volume:
```yaml
volumes:
  - .:/app
```

For production, remove volume mounts and use built image.

### Health Checks

The application includes health checks:
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

## Security Considerations

### Production Security

1. **Use production compose file** with proper security settings
2. **Enable HTTPS** with valid SSL certificates
3. **Use environment variables** for sensitive configuration
4. **Regular security updates** of base images
5. **Set strong passwords** for any additional services (if added)

### Network Security

For single-service applications, Docker Compose automatically creates a default network. For multi-service applications, you can add custom network configuration:

```yaml
networks:
  medinext-network:
    driver: bridge
    # Add custom network configuration for production
```

### User Permissions

The container runs as non-root user:
```dockerfile
RUN useradd --create-home --shell /bin/bash streamlit
USER streamlit
```

## Monitoring and Logging

### Log Management

```bash
# View application logs
docker-compose logs -f manufacturing-ai

# View all service logs
docker-compose logs -f

# Export logs to file
docker-compose logs > app.log
```

### Health Monitoring

```bash
# Check service health
docker-compose ps

# Health check endpoint
curl http://localhost:8501/_stcore/health
```

## Support

For Docker-related issues:

1. Check this documentation
2. Review Docker logs: `docker-compose logs`
3. Check container status: `docker-compose ps`
4. Verify Docker installation: `docker --version`
5. Check Docker Desktop status

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Streamlit Docker Guide](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-using-docker)
