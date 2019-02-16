import os
from flask import Flask, render_template, request, make_response
from model import db, app, InventoryItem

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Get and post methods to get iD and return rendered html report
@app.route('/form4pdf', methods=['GET', 'POST'])
def sitepdf():
    id = None
    if(request.method == 'POST'):
        id = request.form.get('id')
        event= db.session.query(InventoryItem).filter(InventoryItem.id == id).all()
        rown = []
        rowp = []
        row_name = map(lambda x: x.name, event)
        row_price = map(lambda x: x.price, event)
        for row in row_name:
            rown.append(row)
            #print(row)
        for row in row_price:
            rowp.append(row)
            #print(row)
     """ Alternative for light data application, this gives name and price without the list. 
        event= db.session.query(InventoryItem).filter(InventoryItem.id == id)
        return render_template('form4pdf.html', row_name=event[0].name, row_price=event[0].price)
     """
     """ pdf can be created from here directly also.
         Debug particular values to be returned
        #import pdb; pdb.set_trace()
        #return pdfkit.from_string(rendered_template, False, css='./static/styles.css')
     """
    return render_template('form4pdf.html', row_name=rown, row_price=rowp)

#convert redered html to pdf format 
@app.route('/form4pdf2', methods=['GET', 'POST'])
def pdfview():
    rendered_template = render_template('form4pdf.html') 
    rendered_template = rendered_template.encode('utf-8') 
    pdf = pdfkit.from_string(rendered_template, False, css='./static/styles.css') 
    return make_response(pdf)

if __name__ == '__main__':

  # run app
    app.run()