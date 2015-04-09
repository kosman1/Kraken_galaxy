How to test Kraken in your local galaxy instance:

In your galaxy home directory config/tool_conf.xml file, change  

```
 <section name="Kraken-test" id="kraken">
    <tool file="/full-path/Kraken_galaxy/kraken.xml" />
	<tool file="/full-path/Kraken_galaxy/kraken-build.xml" />
    <tool file="/full-path/Kraken_galaxy/kraken-report.xml" />
</section>
 ```

In the config/tool_data_table_conf.xml, add this:

```
<table name="krakendb" comment_char="#">
    <columns>value ,dbkey, display_name, file_path</columns>
    <file path="/full-path/Kraken_galaxy/tool-data/kraken_database.loc" />
</table>
```

TODO: 

1. Fix kraken.xml to take in fastq files- it does, but fails to recognize files with reads below a certain length

2. Kraken-report is not finding 'kraken' -  
File "DynamicallyCompiledCheetahTemplate.py", line 94, in respond
NotFound: cannot find 'kraken

3. Make sequence filtering work.

4. Kraken-build