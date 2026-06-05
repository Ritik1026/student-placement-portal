# Placement Portal Frontend

React-based frontend for the student placement portal.

## Features

- Student dashboard for resume upload
- Company dashboard for job posting and candidate browsing
- Authentication pages (Login/Register)
- Responsive design with Tailwind CSS
- Redux state management

## Technology Stack

- **Framework**: React 18
- **Routing**: React Router v6
- **Styling**: Tailwind CSS
- **State Management**: Redux / Context API
- **HTTP Client**: Axios

## Installation

```bash
cd frontend
npm install
```

## Environment Variables

Create a `.env` file in the frontend directory:

```
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ENV=development
```

## Running the Application

### Development

```bash
npm start
```

The application will open at `http://localhost:3000`

### Build for Production

```bash
npm run build
```

### Testing

```bash
npm test
```

## Project Structure

```
src/
├── pages/
│   ├── Home.js
│   ├── Login.js
│   ├── Register.js
│   ├── StudentDashboard.js
│   └── CompanyDashboard.js
├── components/
│   └── Navbar.js
├── services/
│   └── api.js (to be created)
├── App.js
└── index.js
```

## Pages

### Home
Landing page introducing the platform to students and companies.

### Login
User login page for students and companies.

### Register
User registration with role selection (Student/Company).

### Student Dashboard
- Resume upload
- AI quality analysis
- View feedback and suggestions
- Job search and applications

### Company Dashboard
- Post new jobs
- View job listings
- Browse shortlisted candidates
- Manage applications

## Development

Make sure the backend API is running on `http://localhost:5000`

## Deployment

### Docker

```bash
docker build -f Dockerfile.dev -t placement-frontend .
docker run -p 3000:3000 placement-frontend
```

### Vercel/Netlify

1. Connect your GitHub repository
2. Set environment variables
3. Deploy
