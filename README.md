# TECHNICAL TEST

## Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## Question C

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

1 - Simplicity. Integration needs to be dead simple.
2 - Resilient to network failures or crashes.
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
4 - Data consistency across regions
5 - Locality of reference, data should almost always be available from the closest region
6 - Flexible Schema
7 - Cache can expire 

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of. When submitting your code add the necessary documentation to explain your overall design and missing functionalities. Do it to the best of your knowledge. Good Luck, you can write it in the language of your choice, name the test using the convention firstname_lastname_test and provide a link in your personal github so we can review the work.

---


# QuestionA: Line Segment Overlap Checker

This Python project contains a script to check if two line segments on the x-axis overlap or touch each other.

## Usage

### Prerequisites

Make sure you have Python3 installed on your system.

### Running the Tests

To run the test cases, execute the `run_tests.sh` shell script:
```bash
./run_tests.sh
```
<img width="659" alt="image" src="https://github.com/Bipinjot/Ormuco/assets/25786623/1a56ae43-2f13-49f8-a41d-7984957e5361">


# QuestionB: String Versin Checker

This Python project contains a script to check if two version string as input and returns whether one is greater than, equal, or less than the other

## Usage

### Prerequisites

Make sure you have Python3 installed on your system.

### Running the Tests

To run the test cases, execute the `run_tests.sh` shell script:
```bash
./run_tests.sh
```
<img width="613" alt="image" src="https://github.com/Bipinjot/Ormuco/assets/25786623/ab1ede44-be67-45e2-b96a-ad533e7640ab">

# QuestionC: Geo Distributed LRU Cache

This Python project contains implementation of LRU Cache based on the requirements of the question.

#### Simplicity - Integration needs to be dead simple:
The implementation follows a straightforward approach with a single class GeoLRUCache that encapsulates the functionality of a Geo Distributed LRU cache. The class provides methods for caching, data retrieval, expiration, and data replication across geolocations. Integration with other components or services can be achieved by instantiating and using this class.

#### Resilient to network failures or crashes:
The code includes error handling in the simulate_data_replication method to catch network failures or crashes during data replication. When a network failure occurs, an exception is raised and handled gracefully, preventing the failure from affecting the cache's functionality.

#### Near real-time replication of data across Geolocation. Writes need to be in real time:
The simulate_data_replication method simulates near real-time data replication across different geolocations. It updates replicated data structures for each region with a slight delay to mimic network latency, ensuring that data replication occurs almost immediately after a write operation.

#### Data consistency across regions:
Data consistency across regions is maintained through the replicated_data dictionary within the GeoLRUCache class. Each region has its replicated data structure, ensuring that data remains consistent across regions despite network latencies or failures.

#### Locality of reference, data should almost always be available from the closest region:
The simulation of data replication across regions implies that data is available in each region's replicated data structure, facilitating quick access and reducing latency for data retrieval.

#### Flexible Schema:
The implementation allows flexibility in terms of the schema used for caching data. It supports key-value pairs where the keys are strings and the values can be of any type, allowing for a flexible data schema based on application requirements.

#### Cache can expire:
The expire_cache method in the GeoLRUCache class handles cache expiration by removing items that have exceeded a specified expiration time. This ensures that the cache remains manageable and avoids storing stale data beyond its useful lifespan.

Simulating LRU Cache different geolocations within the scope of a single Python script can be challenging because it typically involves network communication, asynchronous messaging, and potentially complex distributed systems concepts. However, I have create a simplified simulation within the code to mimic the concept of data replication across regions.

## Usage

### Prerequisites

Make sure you have Python3 installed on your system.

### Running the Tests

To run the test cases, execute the `run_tests.sh` shell script:
```bash
./run_tests.sh
```
<img width="629" alt="image" src="https://github.com/Bipinjot/Ormuco/assets/25786623/0cd0747a-97d0-4e0c-8612-45bb4da822f4">
