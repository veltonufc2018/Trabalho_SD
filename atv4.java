import java.io.*;
import java.net.*;
import java.util.*;

public class VotingServer {
    private static List<Candidate> candidates = new ArrayList<>();

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Server started. Listening on port 12345...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                ClientHandler clientHandler = new ClientHandler(clientSocket);
                clientHandler.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class ClientHandler extends Thread {
        private Socket clientSocket;
        private DataInputStream in;
        private DataOutputStream out;

        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }

        @Override
        public void run() {
            try {
                in = new DataInputStream(clientSocket.getInputStream());
                out = new DataOutputStream(clientSocket.getOutputStream());

                String clientType = in.readUTF();
                if (clientType.equals("Elector")) {
                    handleElector();
                } else if (clientType.equals("Admin")) {
                    handleAdmin();
                }

                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        private void handleElector() throws IOException {
            out.writeUTF("Welcome, Elector. Here is the list of candidates:");
            for (Candidate candidate : candidates) {
                out.writeUTF(candidate.getName());
            }

            String vote = in.readUTF();
            // Record the vote and perform necessary operations.
        }

        private void handleAdmin() throws IOException {
            out.writeUTF("Bem vindo");
            out.writeUTF("1. Add usuario");
            out.writeUTF("2. Remove usuario");
            out.writeUTF("3. Envia");

            int choice = in.readInt();
            switch (choice) {
                case 1:
                    // Add a new candidate
                    String candidateName = in.readUTF();
                    candidates.add(new Candidate(candidateName));
                    out.writeUTF("usuario add.");
                    break;
                case 2:
                    // Remove a candidate
                    String candidateToRemove = in.readUTF();
                    candidates.removeIf(candidate -> candidate.getName().equals(candidateToRemove));
                    out.writeUTF("Usuario removido.");
                    break;
                case 3:
                    // Send a note to electors via multicast (UDP)
                    // Implement multicast logic here
                    break;
                default:
                    out.writeUTF("ivalido.");
                    break;
            }
        }
    }
}

class Candidate {
    private String name;
    private int votes;

    public Candidate(String name) {
        this.name = name;
        this.votes = 0;
    }

    public String getName() {
        return name;
    }

    public int getVotes() {
        return votes;
    }

    public void incrementVotes() {
        votes++;
    }
}
