import { createClient } from "gel"; // or "edgedb"
import e from "./dbschema/edgeql-js";

const client = createClient();

// The return type of 'result' is automatically inferred as a string
const result = await e.select("Hello world!").run(client); 

