import { useState } from "react";
import "axios";
import axios from "axios";
import { apiUrl } from "./config";

function App() {
  const inputStyles = {
    width: "100%",
    padding: "1.5rem 1rem",
    borderRadius: "12px",
    border: "none",
  };

  // Price History Form
  const [coin_name_price, setCoinNamePrice] = useState("");
  const [price_data, setPriceData] = useState(null);

  // Subscription Form
  const [email, setEmail] = useState("");
  const [coin_name_subscription, setCoinName] = useState("");
  const [difference_percentage, setDifferencePercentage] = useState(0);

  function handlePriceForm(e) {
    e.preventDefault();
    axios.post(apiUrl + "price/", {
        coin_name: coin_name_price
      }
    ).then((res) => {
        if (res.status) {
          setPriceData(res.data.message);
        }
      }
    ).catch((err) => {
        alert(err.response.data.message);
      }
    );
  }

  function handleSubscriptionForm(e) {
    e.preventDefault();
    axios.post(
      apiUrl + "subscribe/", 
      {
        email: email,
        coin_name: coin_name_subscription,
        difference_percentage: difference_percentage,
      }
    ).then((res) => {
        if (res.status) {
          alert(res.request.response);
        }
      }
    ).catch((err) => {
        alert(err.response.data.message);
      }
    );
  }
  
  return (
    <div>
      <div
        style={{
          width: "80vw",
          height: "80vh",
          display: "flex",
          alignItems: "start",
        }}
      >
        <div
          style={{
            width: "70%",
            padding: "0 10%",
          }}
        >
          <form
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "2rem",
              textAlign: "center",
            }}
            onSubmit={handlePriceForm}
          >
            <h2>Price History Form</h2>
            <input
              style={inputStyles}
              type="text"
              placeholder="Coin Name"
              value={coin_name_price}
              onChange={(e) => setCoinNamePrice(e.target.value)}
              required
            />
            <input
              style={{
                ...inputStyles,
                boxSizing: "content-box",
                cursor: "pointer",
                backgroundColor: "#50b",
              }}
              type="submit"
              value="Submit"
            />
          </form>
          {price_data?.map((item, index) => (
            <div key={index}>
              <span>{item.coin_name} / {item.price} / {item.time_stamp}</span>
            </div>
          ))}
        </div>
        <div
          style={{
            width: "30%",
          }}
        >
          <form
            style={{
              display: "flex",
              flexDirection: "column",
              textAlign: "center",
              gap: "1rem",
            }}
            onSubmit={handleSubscriptionForm}
          >
            <h2>Subscription Form</h2>
            <input
              style={inputStyles}
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              style={inputStyles}
              type="text"
              placeholder="Coin Name"
              value={coin_name_subscription}
              onChange={(e) => setCoinName(e.target.value)}
              required
            />
            <input
              style={inputStyles}
              placeholder="Percentage"
              type="number"
              value={difference_percentage}
              min={0}
              max={100}
              onChange={(e) => setDifferencePercentage(e.target.value)}
              required
            />
            <input
              style={{
                ...inputStyles,
                boxSizing: "content-box",
                cursor: "pointer",
                backgroundColor: "#50b",
              }}
              type="submit"
              value="Submit"
            />
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
