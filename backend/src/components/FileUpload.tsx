import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { Upload } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";

interface FileUploadProps {
  onUpload: (file: File) => Promise<void>;
  isLoading: boolean;
}

export const FileUpload = ({ onUpload, isLoading }: FileUploadProps) => {
  const [uploadProgress, setUploadProgress] = useState(0);

  const onDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (file) {
      // Simulate upload progress
      const interval = setInterval(() => {
        setUploadProgress(prev => {
          if (prev >= 100) {
            clearInterval(interval);
            return 100;
          }
          return prev + 10;
        });
      }, 200);

      await onUpload(file);
      clearInterval(interval);
      setUploadProgress(0);
    }
  }, [onUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf']
    },
    maxFiles: 1,
    disabled: isLoading
  });

  return (
    <div>
      <div
        {...getRootProps()}
        className={`drop-zone ${isDragActive ? 'active' : ''} ${
          isLoading ? 'opacity-50 cursor-not-allowed' : ''
        }`}
      >
        <input {...getInputProps()} />
        <Upload className="w-12 h-12 mb-4 mx-auto text-primary" />
        <p className="text-lg mb-2">
          {isDragActive
            ? "Drop your bank statement here"
            : "Drag & drop your bank statement here"}
        </p>
        <p className="text-sm text-muted-foreground mb-4">
          or click to select file
        </p>
        <Button variant="outline" disabled={isLoading}>
          Select PDF File
        </Button>
      </div>

      {isLoading && (
        <div className="mt-4">
          <Progress value={uploadProgress} className="mb-2" />
          <p className="text-sm text-center text-muted-foreground">
            Analyzing your bank statement...
          </p>
        </div>
      )}
    </div>
  );
};