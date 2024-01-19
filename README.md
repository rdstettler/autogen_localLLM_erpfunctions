# Autogen using functions and a local LLM
Example of how to use a local llm with function calling, in this example to call local (company) ERP systems

# Local LLM
I just started a local API with llama_cpp.server like this

>  python -m llama_cpp.server --model C:\pathto\mistral-7b-instruct-v0.2.Q4_K_M.gguf --n_ctx 4096 --main_gpu 0 --n_gpu_layers -1

It listenes to localhost:8000

# Results using OpenAI ChatGPT3.5

user_proxy (to assistant):

What name does workcenter 511V0001 have? 

--------------------------------------------------------------------------------
assistant (to user_proxy):

***** Suggested function Call: get_description_of_workcenter *****
Arguments: 
{
  "workcenter_id": "511V0001"
}
******************************************************************

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_description_of_workcenter...
user_proxy (to assistant):

***** Response from calling function "get_description_of_workcenter" *****
Verpackungsanlage 441
**************************************************************************

--------------------------------------------------------------------------------
assistant (to user_proxy):
...

The workcenter 511V0001 is named "Verpackungsanlage 441". TERMINATE

--------------------------------------------------------------------------------

# Result using mistral instruct

user_proxy (to assistant):

What name does workcenter 511V0001 have? 

--------------------------------------------------------------------------------
assistant (to user_proxy):

 To get the description of workcenter with ID '511V0001', you can use the `get_description_of_workcenter` function as follows:

```python
workcenter_description = get_description_of_workcenter('511V0001')
print(f"Workcenter ID 511V0001 has the name or description: {workcenter_description}")
```

To get the current order data for workcenter with ID '511V0001', you can use the `get_current_orderdata_for_workcenter` function as follows:

```python
order_data = get_current_orderdata_for_workcenter('511V0001')
print(f"Current order data for workcenter ID 511V0001 is: {order_data}")
```

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
SIGALRM is not supported on Windows. No timeout will be enforced.
user_proxy (to assistant):

exitcode: 1 (execution failed)
Code output: 
Traceback (most recent call last):
  File "", line 1, in <module>
    workcenter_description = get_description_of_workcenter('511V0001')
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'get_description_of_workcenter' is not defined


--------------------------------------------------------------------------------
