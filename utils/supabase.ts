
import { createClient } from "@supabase/supabase-js";

const supabaseUrl = process.env.https://nulgqjqsqiokhobbhzce.supabase.co;
const supabaseKey = process.env.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im51bGdxanFzcWlva2hvYmJoemNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIyOTY4ODEsImV4cCI6MjA1Nzg3Mjg4MX0.2MTbOasHr_oxQZXjcndjmp5sR6gUOmYG7LHVb6bZFS8;

export const supabase = createClient(supabaseUrl, supabaseKey);
        
