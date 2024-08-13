# IoT Policy Language Tutorial

## Introduction

In IoT defenses, natural language can be structured into a format that is easily parseable. This tutorial explores how to convert English statements into a policy language using logical expressions and variables.

## Logical Expressions and Variables

Consider the statement: "If Fire Sprinkler is on, then Water Valve is on." This can be expressed as:

```
If FireSprinkler.status == "ON" Then WaterValve.status == "ON"
```

However, for improved readability, we can assign the logical expression into a variable and use the variable in policy statement. The above policy statement can be re-written as follows.

```
If FireSprinklerOn Then WaterValveOn

FireSprinklerOn = (FireSprinkler.status == "ON")
WaterValveOn = (WaterValve.status == "ON")
```

## Device attributes

In the above example, we used `status` attribute of `FireSprinkler` and `WaterValve` devices. You can use other device attributes as well.

## Functions

Besides device attibutes, function calls can be employed in logical expressions. For example, we can use `timer(logical_expression)` function.
We assume that the `timer` function returns the elapsed time since the logical expression became true.

#### Text
"If water leak sensor sensed wet within 1 minute, then turn off water sprinkler."

#### Policy

```
If (timer(WaterLeakSensorWet) > 0 and timer(WaterLeakSensorWet) < 60) Then WaterSprinklerOn

WaterLeakSensorWet = (WaterLeakSensor.status == "Wet")
WaterSprinklerOn = (WaterSprinkler.status == "On")
```

This example demonstrates the use of the timer function to determine if a condition occurred within a specified time frame.

## Logical Operators

In the above example, we used `and` operator to combine multiple expressions. Some other operators like `or` and `not` also can be used.

#### Text
If User Away, on Vacation or Sleeping Then Gas Stove is off

#### Policy

```
If Away or Vacation or Sleep Then GasStoveOff

Away = (HomeMode.status == "Away")
Vacation = (Vacation.status == "True")
Sleep = (HomeMode.status == "Sleep")
GasStoveOff = (GasStove.status == "Off")
```

This example uses the `or` operator to ensure at least one of the conditions are satisfied.

## Unique Policies

### Policies with "Only If"

Statements like "X only if Y" are equivalent to "If X Then Y"

#### Text

Light can be switched on only if the user is at home.

#### Policy

```
If LightOn Then HomeModeHome  

LightOn = (Light.status == "ON")
HomeModeHome = (HomeMode.status == "home")
```

### Policies with "Allow"

Convert "Allow" statements to the standard policy format

#### Text
Allow living room window to be opened only if both heater and AC are off.

#### Policy
```
If LivingRooomWindowOpen Then (HeaterOff and ACOff)
        
LivingRooomWindowOpen = (LivingRoomWindow.status == "Open")
ACOff = (AC.status == "Off")
HeaterOff = (Heater.status == "Off")
```

### Policies with "Deny"

For "Deny" statements, remove "Deny" and apply the `not` operator to the conclusion.

#### Text
Deny turning on the coffee machine only if the user is on a vacation.

#### Policy
```
If CoffeeMachineOn Then not(Vacation)

CoffeeMachineOn = (CoffeeMachine.status == "On")
Vacation = (Vacation.status == "True")
```

### Policies with "when"

"when" is equivalent to "if". Consider "when" as "if" and apply standard translation rule.

#### Text

The bell must not chime when the door is closed.

#### Policy

```
If DoorClosed Then not(BellChime)

DoorClosed = (Door.status == "Closed")
BellChime = (Bell.status == "Chime")
```

### Temporal Operators

Operators **since** and **yesterday** deal with temporal logic and can be useful for determining the last state of a device. Examples include:

#### Text
Allow turning off coffee machine only if lastly it was on.

#### Policy
```
If CoffeeMachineOff Then yesterday CoffeeMachineOn

CoffeeMachineOff = (CoffeeMachine.status == "Off")
CoffeeMachineOn = (CofeeMachine.status == "On")
```

#### Text
Allow irrigation to go off only if it has been dry within 2 days since moisture sensor sensed wet

#### Policy
```
If IrrigationSprinklerOn Then (timer(GardenMoistureSensorDry) > 0 and timer(GardenMoistureSensorDry) < 172800) since GardenMoistureSensorWet

IrrigationSprinklerOn = (IrrigrationSprinkler.status == "On")
GardenMoistureSensorDry = (GardenMoistureSensor.status == "Dry")
GardenMoistureSensorWet = (GardenMoistureSensor.status == "Wet")
```

### Perpetually Valid

There are instances where a logical expression needs to be consistently true. In such scenarios, the `true`` keyword should be employed within the if condition.

#### Text

In any situation, surveillance camera must remain on.

#### Policy

```
If true Then SurvellianceCameraOn

SurvellianceCameraOn = (SurvellianceCamera.status == "On")
```

## Conclusion

By following these guidelines, you can effectively translate natural language statements into a policy language suitable for IoT defenses.
