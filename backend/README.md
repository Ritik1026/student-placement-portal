# Placement Portal Backend

RESTful API for the student placement portal with user authentication, resume management, and job posting.

## Features

- User authentication (Student, Company, Admin)
- Resume upload and management
- Job posting and application
- Integration with AI service for resume analysis
- JWT-based authentication

## Technology Stack

- **Framework**: Express.js
- **Database**: MongoDB
- **Caching**: Redis
- **Authentication**: JWT
- **File Upload**: Multer

## Installation

```bash
cd backend
npm install
```

## Environment Variables

Create a `.env` file in the backend directory:

```
BACKEND_PORT=5000
NODE_ENV=development
JWT_SECRET=your_jwt_secret_key
MONGODB_URI=mongodb://localhost:27017/placement_portal
REDIS_URL=redis://localhost:6379
```

## Running the Server

### Development

```bash
npm run dev
```

### Production

```bash
npm start
```

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Students

- `GET /api/students/:id` - Get student profile
- `PUT /api/students/:id` - Update student profile

### Companies

- `GET /api/companies/:id` - Get company profile
- `POST /api/companies/:id/jobs` - Post job

### Jobs

- `GET /api/jobs` - Get all active jobs
- `GET /api/jobs/:id` - Get job details

### Resumes

- `POST /api/resumes/upload` - Upload resume
- `GET /api/resumes/student/:studentId` - Get student resumes

### Shortlist

- `GET /api/shortlist/job/:jobId` - Get shortlisted candidates
- `POST /api/shortlist` - Add to shortlist

## Development

Make sure MongoDB and Redis are running:

```bash
# MongoDB
mongod

# Redis (in another terminal)
redis-server
```

Or use Docker:

```bash
docker-compose up -d mongodb redis
```

## Testing

```bash
npm test
```

## Linting

```bash
npm run lint
```
