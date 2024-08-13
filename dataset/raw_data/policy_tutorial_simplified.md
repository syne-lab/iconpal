# Simplified IoT Policy Language Tutorial

## Introduction

In IoT defense, we can structure everyday language into a format that computers can understand easily. This guide shows you how to convert English statements into a policy language using logical expressions and variables.

## Logical Expressions and Variables

Take a sentence like "If the Fire Sprinkler is on, then the Water Valve is on." This can be written as:

```plaintext
If FireSprinkler.status == "ON" Then WaterValve.status == "ON"
```

For better readability, you can use variables:

```plaintext
If FireSprinklerOn Then WaterValveOn

FireSprinklerOn = (FireSprinkler.status == "ON")
WaterValveOn = (WaterValve.status == "ON")
```

## Device Attributes

You can use various attributes of devices, not just `status`.

## Functions

Functions like `timer(logical_expression)` can be used to introduce time-based conditions.

```plaintext
If (timer(WaterLeakSensorWet) > 0 and timer(WaterLeakSensorWet) < 60) Then WaterSprinklerOn

WaterLeakSensorWet = (WaterLeakSensor.status == "Wet")
WaterSprinklerOn = (WaterSprinkler.status == "On")
```

## Logical Operators

Use operators like `and`, `or`, and `not` to combine or negate conditions.

```plaintext
If Away or Vacation or Sleep Then GasStoveOff

Away = (HomeMode.status == "Away")
Vacation = (Vacation.status == "True")
Sleep = (HomeMode.status == "Sleep")
GasStoveOff = (GasStove.status == "Off")
```

## Unique Policies

### "Only If" Statements

Statements like "X only if Y" are equivalent to "If X Then Y."

```plaintext
If LightOn Then HomeModeHome  

LightOn = (Light.status == "ON")
HomeModeHome = (HomeMode.status == "home")
```

### "Allow" Statements

Convert "Allow" statements to standard policy format.

```plaintext
If LivingRoomWindowOpen Then (HeaterOff and ACOff)
        
LivingRoomWindowOpen = (LivingRoomWindow.status == "Open")
ACOff = (AC.status == "Off")
HeaterOff = (Heater.status == "Off")
```

### "Deny" Statements

For "Deny" statements, remove "Deny" and use the `not` operator.

```plaintext
If CoffeeMachineOn Then not(Vacation)

CoffeeMachineOn = (CoffeeMachine.status == "On")
Vacation = (Vacation.status == "True")
```

### "When" Statements

"when" is equivalent to "if". Consider "when" as "if" and apply standard translation rule.

For example, "The bell must not chime when the door is closed." can be written as 

```plaintext
If DoorClosed Then not(BellChime)

DoorClosed = (Door.status == "Closed")
BellChime = (Bell.status == "Chime")
```
### Temporal Operators

Operators like **since** and **yesterday** handle temporal logic.

```plaintext
If CoffeeMachineOff Then yesterday CoffeeMachineOn

CoffeeMachineOff = (CoffeeMachine.status == "Off")
CoffeeMachineOn = (CofeeMachine.status == "On")
```

```plaintext
If IrrigationSprinklerOn Then (timer(GardenMoistureSensorDry) > 0 and timer(GardenMoistureSensorDry) < 172800) since GardenMoistureSensorWet

IrrigationSprinklerOn = (IrrigrationSprinkler.status == "On")
GardenMoistureSensorDry = (GardenMoistureSensor.status == "Dry")
GardenMoistureSensorWet = (GardenMoistureSensor.status == "Wet")
```

### Perpetually Valid

For always-true conditions, use the `true` keyword within the if condition.

```plaintext
If true Then SurvellianceCameraOn

SurveillanceCameraOn = (SurveillanceCamera.status == "On")
```

## Conclusion

Follow these guidelines to easily translate natural language into a policy language suitable for IoT defenses.