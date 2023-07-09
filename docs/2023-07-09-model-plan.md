# Models

## Apparel

> Purpose: Make laundry easier by making it a tracked/data problem.
> - Create an inventory of clothes
> - Create a log of when clothes are worn and washed

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
- apparel/wearCollection
    - Contains all wearLogs for a given user
- apparel/washEntry
    - Instance of apparel being washed in time
- apparel/washLog
    - Contains multiple washEntries for a given day
- apparel/washCollection
    - Contains all washLogs for a given user

---

## Fitness

- fitness/exercise
    - Set of all exercises
- fitness/exerciseEntry
    - Instance of performing an exercise in time at a specified weight by a given user
- fitness/exerciseLog
    - Contains all exerciseEntries for a given day and user
- fitness/exerciseCollection
    - Contains all exerciseLogs for a given user

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
- food/foodCollection
    - Contains all foodLogs for a given user

---

(mirrors fitness/exerciseProgram)

- food/mealPlan
    - Contains mealPlanEntries
- food/mealPlanEntry
    - Similar to mealEntry w/o time or user information, and specific to parent mealPlan

---

- food/groceryList
    - Contains groceryListEntries
- food/groceryListEntry
    - Contains food and quantity
- food/groveryListCollection
    - Contains all groveryLists for a given user

---

- food/inventory
    - Contains inventoryEntries
- food/inventoryEntry
    - Food and quantity (+/-)
- food/inventoryCollection
    - Contains all inventories for a given user

---

## Parts

- parts/entry
    - Name, type, description, notes - Instance of a part in time

---

## Shared

> Purpose: Used for any models that are shared across applications

- shared/TBD

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

---

- stocks/buy
    - An entry at which stock is bought in time
- stocks/sell
    - An entry at which stock is sold in time

---

## Weight

- weight/entry
    - A measured weight in time
- weight/log
    - Contains entries for a given day and user
- weight/collection
    - Contains all logs for a given user

---

## Wishlist

- wishlist/entry
    - An addition to a wishlist. Simple name/description + some timing meta data
- wishlist/collection
    - Contains all entries for a given user
