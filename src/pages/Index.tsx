import { useState } from "react";
import { FileUpload } from "@/components/FileUpload";
import { ResultsDashboard } from "@/components/ResultsDashboard";
import { toast } from "sonner";
import { ThemeToggle } from "@/components/theme-toggle";

interface AnalysisResult {
  qualificationScore: number;
  monthlyIncome: number[];
  monthlyExpenses: number[];
  balanceTrend: number[];
  months: string[];
}

// Placeholder data for demonstration
const placeholderResults: AnalysisResult = {
  qualificationScore: 85,
  monthlyIncome: [5000, 5500, 4800, 5200, 5400, 5800, 5600, 5900, 6000, 5800, 6200, 6500],
  monthlyExpenses: [3000, 3200, 2900, 3100, 3300, 3400, 3200, 3500, 3400, 3300, 3600, 3800],
  balanceTrend: [2000, 2300, 1900, 2100, 2100, 2400, 2400, 2400, 2600, 2500, 2600, 2700],
  months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
};

const Index = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState<AnalysisResult | null>(null);

  const handleFileUpload = async (file: File) => {
    setIsLoading(true);
    try {
      // Simulated API call - replace with your actual backend endpoint
      await new Promise(resolve => setTimeout(resolve, 2000));
      setResults(placeholderResults);
      toast.success("Bank statement analysis complete!");
    } catch (error) {
      toast.error("Failed to analyze bank statement. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-8 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">
          Loan Qualification Analysis
        </h1>
        <ThemeToggle />
      </div>
      
      {!results && (
        <div className="max-w-xl mx-auto">
          <p className="text-center text-muted-foreground mb-8">
            Upload your bank statement (PDF) to analyze your loan qualification
          </p>
          <FileUpload onUpload={handleFileUpload} isLoading={isLoading} />
        </div>
      )}
      
      {results && <ResultsDashboard results={results} onReset={() => setResults(null)} />}
    </div>
  );
};

export default Index;