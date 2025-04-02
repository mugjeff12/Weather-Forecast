# 🌦️ Weather Forecast Web App

Welcome to the **Weather Forecast App** – a simple yet powerful web application built with **Streamlit** and **Plotly**, providing real-time weather forecasts for the next 1–5 days.

 
📁 **Repo:** [github.com/mugjeff12/Weather-Forecast](https://github.com/mugjeff12/Weather-Forecast)

---

## 🚀 Features

- 🔍 Search for any **city/place** in the world.
- 📅 Select how many days to forecast (1 to 5).
- 📊 View real-time **temperature trends** in interactive line charts.
- ☁️ Visualize **sky conditions** (Clear, Clouds, Rain, Snow) with custom icons.
- 💡 Clean and interactive UI powered by **Streamlit**.

---

## 🧠 Tech Stack

| Tech        | Purpose                      |
|-------------|------------------------------|
| Streamlit   | Web app framework            |
| Plotly      | Interactive data visualization |
| Python      | Logic and backend            |
| OpenWeatherMap API *(assumed)* | Weather data source |
| PNG Icons   | Represent sky conditions     |

---

## 📁 Project Structure

```
Weather-Forecast/
├── images/
│   ├── clear.png
│   ├── cloud.png
│   ├── rain.png
│   └── snow.png
├── backend.py           # Weather data fetching logic
├── app.py               # Main Streamlit app file
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
```

---

## 💻 How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/mugjeff12/Weather-Forecast.git
cd Weather-Forecast
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 🧪 Sample `requirements.txt`

```
streamlit
plotly
requests
```

Add any other dependencies you use in `backend.py`.

---

## ⚠️ Notes

- The `backend.py` file must contain a function `get_data(place, days)` that returns weather data from a source like the **OpenWeatherMap API**.
- Ensure you have `.png` images in the `/images` directory named exactly as:
  - `clear.png`
  - `cloud.png`
  - `rain.png`
  - `snow.png`

---

## 📌 Screenshots (Optional - Add Here)

You can add preview images or a `.gif` of the app running here to showcase how it works.

---

## ✨ Future Ideas

- Add weather parameters like humidity, wind speed, and UV index.
- Add real-time map view with geolocation.
- Implement dark/light theme toggle.
- Save previous searches or create user profiles.

---

## 👤 Author

Made with ❤️ by [Mugdho Jeferson Rozario](https://github.com/mugjeff12)  
> Engineering Physics student @ McMaster | AI Enthusiast | Python Developer  

---

## 📜 License

This project is licensed under the MIT License – use freely, contribute kindly, and credit responsibly.
