const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());
app.use(cors());

// Environment variable for NLP service URL
const NLP_SERVICE_URL = process.env.NLP_SERVICE_URL || "http://localhost:5001";

app.post('/analyze', async (req, res) => {
    const { emailText } = req.body;
    try {
        const response = await axios.post(`${NLP_SERVICE_URL}/analyze`, { text: emailText });
        res.json(response.data);
    } catch (error) {
        console.error("Error analyzing text:", error);
        res.status(500).send("Error analyzing text");
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
