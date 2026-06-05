const express = require('express');
const router = express.Router();
const Resume = require('../models/Resume');
const multer = require('multer');

const upload = multer({ dest: 'uploads/' });

// Upload resume
router.post('/upload', upload.single('resume'), async (req, res) => {
  try {
    const { studentId } = req.body;
    const resume = new Resume({
      studentId,
      filename: req.file.originalname,
      filePath: req.file.path,
      fileSize: req.file.size,
      contentType: req.file.mimetype
    });
    await resume.save();
    res.json({ message: 'Resume uploaded', resume });
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

// Get student resumes
router.get('/student/:studentId', async (req, res) => {
  try {
    const resumes = await Resume.find({ studentId: req.params.studentId });
    res.json(resumes);
  } catch(err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
