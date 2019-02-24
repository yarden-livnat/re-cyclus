from cyclus_gateway.server import create_server

app = create_server()
app.run(host='0.0.0.0', port=5000, debug=True)

