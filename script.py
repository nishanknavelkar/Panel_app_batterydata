import panel as pn
import pandas as pd
import hvplot.pandas

pn.extension(sizing_mode="stretch_width", template="fast")
pn.state.template.param.update(site="Panel in the Browser", title="EIS viewer Example")

select = pn.widgets.Select(options={
    'Eis': 'eisdata.csv'
})

def add_data(event):
    b = io.BytesIO()
    upload.save(b)
    b.seek(0)
    name = '.'.join(upload.filename.split('.')[:-1])
    select.options[name] = b
    select.param.trigger('options')
    select.value = b
    

def explore(csv):
    df = pd.read_csv(csv)
    explorer = hvplot.explorer(df)
    def plot_code(**kwargs):
        code = f'```python\n{explorer.plot_code()}\n```'
        return pn.pane.Markdown(code, sizing_mode='stretch_width')
    return pn.Column(
        explorer,
        '**Code**:',
        pn.bind(plot_code, **explorer.param.objects())
    )

widgets = pn.Column(
    "Select an existing dataset or upload one of your own CSV files and start exploring your data.",
    pn.Row(
        select,
    )
).servable()  

output = pn.panel(pn.bind(explore, select)).servable()

pn.Column(widgets, output)

pn.template.FastListTemplate(
    site="Panel", 
    title="EIS data viewer", 
    main=[
        "This example creates a dropdown that allows to visualize data from csv."
    ], main_max_width="768px",
).servable();