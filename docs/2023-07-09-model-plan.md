# Models

## Apparel

- apparel/apparel
    - Set of all apparel to a given user
- apparel/outfit
    - Combination of many apparel to a given user

---

- apparel/wearEntry
    - Instance of apparel being worn in time by a user
    - Option to make specified apparel to an outfit
- apparel/wearLog
    - Contains multiple wearEntries for a given day

---

- apparel/washEntry
    - Instance of apparel being washed in time
- apparel/washLog
    - Contains multiple washEntries for a given day

---

## Fitness

- fitness/exercise
    - Set of all exercises
- fitness/exerciseEntry
    - Instance of performing an exercise in time at a specified weight by a given user
- fitness/exerciseLog
    - Contains all exerciseEntries for a given day and user

---

- fitness/exerciseProgram
    - Contains exerciseProgramEntries
- fitness/exerciseProgramEntry
    - Similar to exerciseEntry w/o time or user information, and specific to parent exerciseProgram

---

## Food

- food/food
    - Set of all foods - contains calorie information, serving sizes, etc
- food/meal
    - Combination of foods to create a meal - provides aggregate calorie information, serving sizes, etc
- food/foodEntry
    - Instance of food being consumed in time
- food/mealEntry
    - Instance of meal being consumed in time
- food/foodLog
    - Contains all food/mealEntries for a given day and user

---

(mirrors fitness/exerciseProgram)

- food/mealPlan
    - Contains mealPlanEntries
- food/mealPlanEntry
    - Similar to mealEntry w/o time or user information, and specific to parent mealPlan

---

- food/groceryList
    - Contains foodEntries



- food/inventory
    - Contains inventoryEntries
- food/inventoryInput
- food/inventoryOutput

---

## Parts

- parts/entry
    - Name, type, description, notes - Instance of a part in time

---

## Shared

- shared/
    - Used for any models that are shared across applications
---

## Stocks

- stocks/symbol
    - Set of all lookup symbols in which stock data is derived from
- stocks/service
    - Set of all services to query stock data from
- stocks/export
    - A non-processed export of data
- stocks/data
    - A processed collection of dataEntries
- stocks/dataEntry
    - A row of data
- stocks/buy
    - An entry at which stock is bought in time
- stocks/sell
    - An entry at which stock is sold in time

---

- weight/entry

---

- wishlist/entry
