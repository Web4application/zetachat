
import { createClient } from "@supabase/supabase-js";

const supabaseUrl = process.env.https://nyatadsfrhtbfxfnyldv.supabase.co;
const supabaseKey = process.env.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im55YXRhZHNmcmh0YmZ4Zm55bGR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUwNjY2NzYsImV4cCI6MjA2MDY0MjY3Nn0.xzUU-pmZlrTO-6-TzQu6M3eM_SeSTdjDNIHEiRtPj3Y;

export const supabase = createClient(supabaseUrl, supabaseKey);
        
