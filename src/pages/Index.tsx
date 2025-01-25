import { useState } from "react";
import { FileUpload } from "@/components/FileUpload";
import { ResultsDashboard } from "@/components/ResultsDashboard";
import { toast } from "sonner";

interface AnalysisResult {
  qualificationScore: number;
  monthlyIncome: number[];
  monthlyExpenses: number[];
  balanceTrend: number[];
  months: string[];
}

const Index = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState<AnalysisResult | null>(null);

  const handleFileUpload = async (file: File) => {
    setIsLoading(true);
    try {
      // Simulated API call - replace with your actual backend endpoint
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Simulated response - replace with actual API integration
      const mockResults: AnalysisResult = {
        qualificationScore: 85,
        monthlyIncome: [5000, 5200, 4800, 5100, 5300, 5400],
        monthlyExpenses: [3000, 3100, 2900, 3200, 3100, 3000],
        balanceTrend: [2000, 2100, 1900, 1900, 2200, 2400],
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
      };
      
      setResults(mockResults);
      toast.success("Bank statement analysis complete!");
    } catch (error) {
      toast.error("Failed to analyze bank statement. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-8 max-w-7xl mx-auto">
      <h1 className="text-4xl font-bold text-center mb-8">
        Loan Qualification Analysis
      </h1>
      
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