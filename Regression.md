<img src= "gif\LetsLearn Regression.jpg"  height = 25%, width=25% cite="memegenerator.net" >
<p style="text-align: right">Credit: <cite>memegenerator.net</cite></p>

---

# Regression Analysis

---
<img src="https://i.redd.it/ukunciu03r821.jpg" style="margin: 20 auto;" height = 50%, width=50% cite="https://i.redd.it/ukunciu03r821.jpg" >
<p style="text-align: right">Credit: <cite>redd.it</cite></p>


## **Question: What is regression?**

Regression, my curious companions, is like playing detective with numbers. 
It's a statistical wizardry that sets out on a journey to uncover the secret dance between different variables.
Imagine this voyage as a tipsy traveler trying to saunter in a straight line—it's quite the sight to behold!

Picture our tipsy explorer at the start of their adventure, attempting to follow a path that aligns with their destination.
Much like them, regression endeavors to create a line that best follows the twists and turns of our data points.
But, here's the kicker: just as our traveler might stumble off the intended course, the regression line might not be a flawless match for every data point.

This enchanting line that cozies up to our data points goes by the whimsical name of the "regression line." It's not about perfection; it's about catching the spirit of the journey.
And oh, the predictions it brings! The regression line whispers secrets about one variable based on another.

For instance, think of predicting house prices based on their square footage, or foreseeing a company's sales by peering into their advertising expenses.

Remember, though, that while regression wields powerful magic, it's not a crystal ball.
The regression line won't hug every data point tightly—it's more of a dance partner, twirling through uncertainties.

So, as you encounter the regression line on your journey, think of our tipsy traveler. 
It's just finding its way, painting a rough sketch of the world's secrets.
A wobbly yet wonderful tool to explore the mysteries of numbers and relationships!

---
<img src="https://checkpointech.com/wp-content/uploads/2018/03/Dont-Overlook-Your-Regression-Testing.png" style="margin: 20 auto;" height = 50%, width=50% cite="https://checkpointech.com/wp-content/uploads/2018/03/Dont-Overlook-Your-Regression-Testing.png" >

<p style="text-align: right">Credit: <cite>checkpointech.com</cite></p>

Now, let's bring another adventurous example to life with interactive visuals and code:

Imagine we're treasure hunters, seeking the connection between the number of gold coins and the length of the beard of legendary pirates.
Our data table is our treasure map:

<div style="font-size:5rem;width:100%;text-align:left;">🧐</div>


  
  ```python
    import pandas as pd
 
    data = {
        "Beard Length (inches)": [5, 8, 6, 9, 7, 10, 8.5, 9.5],
        "Gold Coins": [100, 300, 200, 400, 250, 500, 350, 450]
    }
 
    treasure_map = pd.DataFrame(data)
    print(treasure_map)
   ```


```python
import pandas as pd

data = {
    "Beard Length (inches)": [5, 8, 6, 9, 7, 10, 8.5, 9.5],
    "Gold Coins": [100, 300, 200, 400, 250, 500, 350, 450]
}

treasure_map = pd.DataFrame(data)
print(treasure_map)
```

Oh, the tales these numbers tell! But what's the connection between beard length and gold coins? Let's visualize this treasure hunt:
<div style="font-size:5rem;width:100%;text-align:right;"> Python 💻 </div>

```python
import matplotlib.pyplot as plt

plt.scatter(treasure_map["Beard Length (inches)"], treasure_map["Gold Coins"])
plt.xlabel("Beard Length (inches)")
plt.ylabel("Gold Coins")
plt.title("Pirate's Treasure: Beard Length vs. Gold Coins")
plt.show()
```


```python
import matplotlib.pyplot as plt

plt.scatter(treasure_map["Beard Length (inches)"], treasure_map["Gold Coins"])
plt.xlabel("Beard Length (inches)")
plt.ylabel("Gold Coins")
plt.title("Pirate's Treasure: Beard Length vs. Gold Coins")
plt.show()
```

Behold the scatter plot, a canvas painted with dots that hold the stories of pirates and their golden hauls. 
The dots don't follow a strict line, but a wandering journey of beards and coins.

Now, it's time to summon the Regression Sorcerer:

<img src="gif\BountifulSmallBluet-max-1mb.gif" cite="https://images.google.com/" >
<p style="text-align: right">Credit: <cite>google images</cite></p>


Direct Code
---

```python
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(treasure_map[["Beard Length (inches)"]], treasure_map["Gold Coins"])

predicted_coins = regressor.predict(treasure_map[["Beard Length (inches)"]])

plt.scatter(treasure_map["Beard Length (inches)"], treasure_map["Gold Coins"])
plt.plot(treasure_map["Beard Length (inches)"], predicted_coins, color='red')
plt.xlabel("Beard Length (inches)")
plt.ylabel("Gold Coins")
plt.title("Pirate's Treasure: Beard Length vs. Gold Coins with the Regression Line")
plt.show()
```


```python
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(treasure_map[["Beard Length (inches)"]], treasure_map["Gold Coins"])

predicted_coins = regressor.predict(treasure_map[["Beard Length (inches)"]])

plt.scatter(treasure_map["Beard Length (inches)"], treasure_map["Gold Coins"])
plt.plot(treasure_map["Beard Length (inches)"], predicted_coins, color='red')
plt.xlabel("Beard Length (inches)")
plt.ylabel("Gold Coins")
plt.title("Pirate's Treasure: Beard Length vs. Gold Coins with the Regression Line")
plt.show()
```

Voila! The Regression Sorcerer conjures a line that's like a trail through the wilderness of numbers. It doesn't hit every dot but captures the essence of the journey. With a twinkle in its eye, the regression line suggests that as the beard length grows, so does the gold haul.

And there you have it—an adventure in data and regression that uncovers the treasures hidden within the tales of pirates and their legendary beards. So, fellow adventurers, set forth and unravel the mysteries that numbers and relationships hold!

<img src="https://variance.hu/wp-content/uploads/cartoon_guide_regression.png" style="margin: 0 auto;">


Absolutely, my inquisitive friend! Let's embark on a journey through this code—a tale of numbers and predictions that's as enchanting as a magical scroll.

First, we're presented with a map of data—a realm of "Beard Lengths" and "Gold Coins." Imagine these numbers as treasures waiting to be discovered!

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    "Beard Length (inches)": [5, 8, 6, 9, 7, 10, 8.5, 9.5],
    "Gold Coins": [100, 300, 200, 400, 250, 500, 350, 450]
}

# Create a DataFrame from the sample data
treasure_map = pd.Dataunravel the mysteries that lie hidden in the numbers!


```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    "Beard Length (inches)": [5, 8, 6, 9, 7, 10, 8.5, 9.5],
    "Gold Coins": [100, 300, 200, 400, 250, 500, 350, 450]
}

# Create a DataFrame from the sample data
treasure_map = pd.DataFrame(data)
```


We've crafted a magical frame called a DataFrame to hold these treasures. Our adventurers, "Beard Lengths," are labeled as `X`, while the sought-after treasures, "Gold Coins," are known as `y`.

```python
# Separate the features (Beard Length) and the target (Gold Coins)
X = treasure_map[["Beard Length (inches)"]]
y = treasure_map["Gold Coins"]
```



```python
# Separate the features (Beard Length) and the target (Gold Coins)
X = treasure_map[["Beard Length (inches)"]]
y = treasure_map["Gold Coins"]
```


Behold the conjuring of a Linear Regression wizard—a mystical being ready to learn the secrets of the map!

```python
# Initialize the Linear Regression model
regressor = LinearRegression()

# Fit the model to the data
regressor.fit(X, y)
```


```python
# Initialize the Linear Regression model
regressor = LinearRegression()

# Fit the model to the data
regressor.fit(X, y)
```




<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




The incantation is cast! Our wizard has been trained using the knowledge encoded in the map. Now, we harness this newfound wisdom to predict treasures—foretelling the "Gold Coins" values using the "Beard Lengths."

```python
# Predict using the trained model
y_pred = regressor.predict(X)
```


```python
# Predict using the trained model
y_pred = regressor.predict(X)
```


And finally, our sage reveals the magical coefficients—the secrets to deciphering the map's patterns.

```python
# Print the coefficients (slope and intercept)
slope = regressor.coef_[0]
intercept = regressor.intercept_
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
```


```python
# Print the coefficients (slope and intercept)
slope = regressor.coef_[0]
intercept = regressor.intercept_
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
```

    Slope: 75.73
    Intercept: -277.63
    


There you have it, an epic tale of Linear Regression! But remember, this is just a taste of the grand adventures that await on your journey into the realm of data and predictions. 
So go forth, armed with knowledge and curiosity, and unravel the mysteries that lie hidden in the numbers!

Ah, the realm of animation! It's like a spellbinding show where numbers come alive, dancing and weaving a tapestry of knowledge. Let me guide you through creating an animated spectacle to showcase the magic of Linear Regression in action. To start, let's add a "Fun Fact" note that tickles the reader's curiosity:

Fun Fact: Unleash the Magic of Animation!

Did you know that numbers can dance? Linear Regression comes to life in the world of animation, where numbers twirl and predictions shine like stars. Get ready to witness an enchanting display of how the "Beard Lengths" and "Gold Coins" perform their mystical dance, guided by the hand of Linear Regression.

Now, let's delve into the realm of code and animation. Below, I'll show you how to use the Plotly library to create an animated visualization that brings the Linear Regression adventure to life:

## Code Decoded: An Adventure in Numbers
Absolutely, let's add a playful twist to our linear regression exploration! Imagine a world where numbers dance and predictions come to life through interactive animations. Here's how you can represent the same linear regression in a delightful and whimsical manner:

Ahoy, curious minds! Ready your wits, for we're about to decode a mystical incantation—a symphony of code that unravels the secrets of regression.
 Behold the mystical spells, line by line, that conjure the very essence of our magical animations:


```python
# Enchanted tools from the wizards' library
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from IPython.display import display, HTML

# Let's create our tale with sample data—a treasure map of beards and gold
data = {
    "Beard Length (inches)": [5, 8, 6, 9, 7, 10, 8.5, 9.5],
    "Gold Coins": [100, 300, 200, 400, 250, 500, 350, 450]
}
treasure_map = pd.DataFrame(data)

# Introducing the Sorcerer—our Linear Regression model
regressor = LinearRegression()

# Crafting a stage for our animation—creating frames for each act
frames = []
test_errors = []

# Now, let's dive into the enchanted loop
for i in range(len(treasure_map)):
    # Preparing data scrolls for our Sorcerer's performance
    x = treasure_map.iloc[:i+1, 0].values.reshape(-1, 1)
    y = treasure_map.iloc[:i+1, 1].values
    regressor.fit(x, y)
    y_pred = regressor.predict(x)
    mse = mean_squared_error(y, y_pred)
    slope = regressor.coef_[0]
    intercept = regressor.intercept_
    equation = f"y = {slope:.2f}x + {intercept:.2f}"
    
    # Crafting frames for our mesmerizing animation
    frame = go.Frame(
        data=[
            go.Scatter(
                x=treasure_map["Beard Length (inches)"][:i+1],
                y=treasure_map["Gold Coins"][:i+1],
                mode='markers',
                marker=dict(size=10),
                name="Training Data"
            ),
            go.Scatter(
                x=treasure_map["Beard Length (inches)"][:i+1],
                y=y_pred,
                mode='lines',
                line=dict(color='red', width=2),
                name="Regression Line"
            )
        ],
        layout=go.Layout(
            title=f"Training Step {i+1}",
            xaxis_title="Beard Length (inches)",
            yaxis_title="Gold Coins",
            showlegend=True,
            annotations=[
                dict(
                    x=0.05,
                    y=0.9,
                    xref="paper",
                    yref="paper",
                    text=f"Slope: {slope:.2f}<br>Intercept: {intercept:.2f}<br>Error: {mse:.2f}<br>Equation: {equation}",
                    showarrow=False
                )
            ]
        ),
        name=f"Training Step {i+1}"
    )
    frames.append(frame)

    # Creating an unseen test dataset for our Sorcerer
    x_test = np.array([11, 12]).reshape(-1, 1)
    y_test_pred = regressor.predict(x_test)
    test_mse = mean_squared_error([550, 600], y_test_pred)
    test_errors.append(test_mse)

# Let's craft the scenes for our second act—test performance animation
test_frames = []
for i in range(len(treasure_map)):
    x = treasure_map.iloc[:i+1, 0].values.reshape(-1, 1)
    y = treasure_map.iloc[:i+1, 1].values
    y_pred = regressor.predict(x)
    test_frame = go.Frame(
        data=[
            go.Scatter(
                x=treasure_map["Beard Length (inches)"][:i+1],
                y=treasure_map["Gold Coins"][:i+1],
                mode='markers',
                marker=dict(size=10),
                name="Training Data"
            ),
            go.Scatter(
                x=treasure_map["Beard Length (inches)"][:i+1],
                y=y_pred,
                mode='lines',
                line=dict(color='red', width=2),
                name="Regression Line"
            ),
            go.Scatter(
                x=x_test.flatten()[:i+1],
                y=y_test_pred[:i+1],
                mode='markers',
                marker=dict(size=10),
                name="Test Predictions"
            )
        ],
        layout=go.Layout(
            title=f"Test Performance - Step {i+1}",
            xaxis_title="Beard Length (inches)",
            yaxis_title="Gold Coins",
            showlegend=True
        ),
        name=f"Test Performance - Step {i+1}"
    )
    test_frames.append(test_frame)

# Let the grand show begin! Creating the training animation
training_animation = go.Figure(
    data=[
        go.Scatter(
            x=treasure_map["Beard Length (inches)"],
            y=treasure_map["Gold Coins"],
            mode='markers',
            marker=dict(size=10),
            name="Training Data"
        ),
        go.Scatter(
            x=[],
            y=[],
            mode='lines',
            line=dict(color='red', width=2),
            name="Regression Line"
        )
    ],
    layout=go.Layout(
        title="Pirate's Treasure: Beard Length vs. Gold Coins (Training)",
        xaxis_title="Beard Length (inches)",
        yaxis_title="Gold Coins",
        showlegend=True
    ),
    frames=frames
)

# Unveiling the second act—test performance animation
test_animation = go.Figure(
    data=[
        go.Scatter(
            x=treasure_map["Beard Length (inches)"],
            y=treasure_map["Gold Coins"],
            mode='markers',
            marker=dict(size=10),
            name="Training Data"
        ),
        go.Scatter(
            x=[],
            y=[],
            mode='lines',
            line=dict(color='red', width=2),
            name="Regression Line"
        ),
        go.Scatter(
            x=[],
            y=[],
            mode='markers',
            marker=dict(size=10),
            name="Test Predictions"
        )
    ],
    layout=go.Layout(
        title="Pirate's Treasure: Beard Length vs. Gold Coins (Test Performance)",
        xaxis_title="Beard Length (inches)",
        yaxis_title="Gold Coins",
        showlegend=True
    ),
    frames=test_frames
)

# Let's add sliders to our animations for an interactive spectacle
training_animation.update_layout(
    sliders=[
        # Slider configuration for training animation
        # (Code for slider setup for training animation)
        {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Step:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [{
            "args": [[frame.name], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate"}],
            "label": frame.name,
            "method": "animate"
        } for frame in frames]
    }
    ],
)

# Now, let's add sliders for the test performance animation
test_animation.update_layout(
    sliders=[
        # Slider configuration for test performance animation
        # (Code for slider setup for test performance animation)
        {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Step:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [{
            "args": [[frame.name], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate"}],
            "label": frame.name,
            "method": "animate"
        } for frame in test_frames]
    }
    ],
)

# Finally, the climax! Display the enchanting animations in our tome
display(HTML(training_animation.to_html()))
display(HTML(test_animation.to_html()))

# And the final touch—displaying the test errors for each step
print("Test Errors:")
for i, test_error in enumerate(test_errors):
    print(f"Step {i+1}: Test MSE = {test_error:.2f}")

```


```python

```
