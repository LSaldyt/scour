# Scour

Scour is a simple command line script to aid with finding sources for research. 
Essentially, scour lets one organize a topic and collect sources in a searchable persistent database.

To use scour, simply put the scour script in your system's PATH and enable execution for the script:

scour requires python3 as well as a google API

`export PATH=$PATH:/path/to/this/directory/`

## Command line usage:

```
lsaldyt@shiva:~/projects/personal/scour$ scour -h
Select a subcommand of scour to run: 
    begin:
        
                Begin a new topic or sub topic, called [topic]
                If already in a topic, begins a new topic
                Arguments: [topic (str)]
                
    collect:
        
                Collect urls based on a google search with [args]
                Arguments: [*args] # A traditional google search
                
    end:
        
                End the current topic or subtopic
                Arguments: None
                
    load:
        
                Load from a saved project file
                Overwrites current database
                Arguments: [filename (str)]
                
    purge:
        
                DANGEROUS:
                Purge all collected data!!!!!!
                Arguments: None
                
    report:
        
                Generate an HTML report, saved to [filename]
                Arguments: [filename (str)]
                
    review:
        
                Review a particular topic in the project database
                Arguments: [*chain (str(s))]
                
    save:
        
                Create a backup of the project in the specified file
                Arguments: [filename (str)]
                
    show:
        
                Show the current database topic tree
                Arguments: None
                
    switch:
        
                Change to topic to [*chain]
                Arguments: [*chain (str(s))]
```


## Example usage:

```
lsaldyt@shiva:~$ scour purge
Purging all collected data
lsaldyt@shiva:~$ scour begin thesis
Beginning the topic thesis
lsaldyt@shiva:~$ scour show
Current topic: thesis
{'thesis': {}}
lsaldyt@shiva:~$ scour begin renewable-energy-generation
Beginning the topic renewable-energy-generation
lsaldyt@shiva:~$ scour collect @articles "renewable energy" ~generation
Collecting sources for the topic: thesis:renewable-energy-generation
('@articles', 'renewable energy', '~generation')
['"renewable energy"', '~generation']
['articles']
lsaldyt@shiva:~$ scour show
Current topic: thesis:renewable-energy-generation
{'thesis': {'renewable-energy-generation': {'__tags__': [<Tag (thesis:renewable-energy-generation) at 2017-11-02 14:13:32.340080>]}}}
lsaldyt@shiva:~$ scour end
Exiting the topic renewable-energy-generation
lsaldyt@shiva:~$ scour show
Current topic: thesis
{'thesis': {'renewable-energy-generation': {'__tags__': [<Tag (thesis:renewable-energy-generation) at 2017-11-02 14:13:32.340080>]}}}
lsaldyt@shiva:~$ scour begin renewable-energy-storage
Beginning the topic renewable-energy-storage
lsaldyt@shiva:~$ scour collect @articles "renewable energy" ~storage
Collecting sources for the topic: thesis:renewable-energy-storage
('@articles', 'renewable energy', '~storage')
['"renewable energy"', '~storage']
['articles']
lsaldyt@shiva:~$ scour show
Current topic: thesis:renewable-energy-storage
{'thesis': {'renewable-energy-generation': {'__tags__': [<Tag (thesis:renewable-energy-generation) at 2017-11-02 14:13:32.340080>]},
            'renewable-energy-storage': {'__tags__': [<Tag (thesis:renewable-energy-storage) at 2017-11-02 14:14:25.867376>]}}}
lsaldyt@shiva:~$ scour end
Exiting the topic renewable-energy-storage
lsaldyt@shiva:~$ scour end
Exiting the topic thesis
lsaldyt@shiva:~$ scour review thesis
Search results for: ""renewable energy" ~generation" with 16 results:
    https://en.wikipedia.org/wiki/Renewable_energy
    [...]
    https://www.nrel.gov/analysis/re-futures.html
Finished
Search results for: ""renewable energy" ~storage" with 12 results:
    http://www.renewableenergyworld.com/energy-storage.html
    [...]
    http://sdg.iisd.org/news/energy-intensive-industries-emerge-as-drivers-of-renewable-energy-expansion/
Finished
lsaldyt@shiva:~$ scour report
Saved a report to summary.html
```
