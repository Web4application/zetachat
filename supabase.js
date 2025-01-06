
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://ovlusvvwyducpspqbfxn.supabase.co'
const supabaseKey = process.env.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92bHVzdnZ3eWR1Y3BzcHFiZnhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYxOTY5MjMsImV4cCI6MjA1MTc3MjkyM30.Rsmd3VxO4DPf-xkVVekRwHptO0Ey8n-XVVGvX0zVYVI
const supabase = createClient(supabaseUrl, supabaseKey)
