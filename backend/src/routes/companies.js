const express = require('express');
const router = express.Router();

// Get company profile
router.get('/:id', async (req, res) => {
  res.json({ message: 'Get company profile' });
});

// Post job
router.post('/:id/jobs', async (req, res) => {
  res.json({ message: 'Create job posting' });
});

module.exports = router;
