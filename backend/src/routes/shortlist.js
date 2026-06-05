const express = require('express');
const router = express.Router();

// Get shortlisted candidates for a job
router.get('/job/:jobId', async (req, res) => {
  res.json({ message: 'Get shortlisted candidates' });
});

// Shortlist a candidate
router.post('/', async (req, res) => {
  res.json({ message: 'Add to shortlist' });
});

module.module = router;
