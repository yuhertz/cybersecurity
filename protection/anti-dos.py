const rateLimit = require('express-rate-limit');
# type "npm install express-rate-limit" into shell


const app = express();

const limiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 100, // limit each IP to 100 requests per windowMs
});

app.use(limiter);
